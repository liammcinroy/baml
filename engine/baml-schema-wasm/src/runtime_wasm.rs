mod runtime_ctx;
mod runtime_prompt;

use std::{collections::HashMap, path::PathBuf};

use baml_runtime::{BamlRuntime, RenderedPrompt};
use js_sys::{JsString, JSON};
use wasm_bindgen::prelude::*;
use wasm_bindgen_futures::JsFuture;
use web_sys::{Request, RequestInit, RequestMode, Response};

use baml_runtime::InternalRuntimeInterface;

use crate::runtime_wasm::runtime_prompt::WasmPrompt;

#[wasm_bindgen]
pub struct WasmProject {
    root_dir_name: String,
    files: HashMap<String, String>,
}

#[wasm_bindgen]
impl WasmProject {
    #[wasm_bindgen]
    pub fn new(root_dir_name: &str, files: JsValue) -> Result<WasmProject, JsError> {
        let files: HashMap<String, String> =
            serde_wasm_bindgen::from_value(files).map_err(|e| e)?;

        Ok(WasmProject {
            root_dir_name: root_dir_name.to_string(),
            files,
        })
    }

    #[wasm_bindgen]
    pub fn update_file(&mut self, name: &str, content: Option<String>) {
        if let Some(content) = content {
            self.files.insert(name.to_string(), content);
        } else {
            self.files.remove(name);
        }
    }

    #[wasm_bindgen]
    pub fn runtime(&self) -> Result<WasmRuntime, JsError> {
        BamlRuntime::from_file_content(&self.root_dir_name, &self.files)
            .map(|r| WasmRuntime { runtime: r })
            .map_err(|e| wasm_bindgen::JsError::new(&e.to_string()))
    }
}

#[wasm_bindgen]
pub struct WasmRuntime {
    runtime: BamlRuntime,
}

#[wasm_bindgen(getter_with_clone)]
pub struct WasmFunction {
    #[wasm_bindgen(readonly)]
    pub name: String,
}

#[wasm_bindgen]
impl WasmRuntime {
    #[wasm_bindgen]
    pub fn list_functions(&self) -> Vec<WasmFunction> {
        self.runtime
            .internal()
            .ir()
            .walk_functions()
            .map(|f| WasmFunction {
                name: f.name().to_string(),
            })
            .collect()
    }

    #[wasm_bindgen]
    pub fn get_function(&self, name: &str) -> Option<WasmFunction> {
        self.runtime
            .internal()
            .ir()
            .walk_functions()
            .find(|f| f.name() == name)
            .map(|f| WasmFunction {
                name: f.name().to_string(),
            })
    }
}

#[wasm_bindgen]
impl WasmFunction {
    #[wasm_bindgen]
    pub fn render_prompt(
        &self,
        rt: &mut WasmRuntime,
        ctx: &runtime_ctx::WasmRuntimeContext,
        params: JsValue,
    ) -> Result<WasmPrompt, wasm_bindgen::JsError> {
        let params = serde_wasm_bindgen::from_value(params)?;
        let env_vars = rt.runtime.internal().ir().required_env_vars();

        // For anything env vars that are not provided, fill with empty strings
        let mut ctx = ctx.ctx.clone();

        for var in env_vars {
            if !ctx.env.contains_key(var) {
                ctx.env.insert(var.into(), "".to_string());
            }
        }

        rt.runtime
            .internal_mut()
            .render_prompt(&self.name, &ctx, &params)
            .map(|p| p.into())
            .map_err(|e| wasm_bindgen::JsError::new(&e.to_string()))
    }
}

#[wasm_bindgen]
pub fn create_runtime(
    root_dir_name: &str,
    files: JsValue,
) -> Result<WasmRuntime, wasm_bindgen::JsError> {
    let files = serde_wasm_bindgen::from_value(files)?;

    baml_runtime::BamlRuntime::from_file_content(root_dir_name, &files)
        .map(|r| WasmRuntime { runtime: r })
        .map_err(|e| wasm_bindgen::JsError::new(&e.to_string()))
}
