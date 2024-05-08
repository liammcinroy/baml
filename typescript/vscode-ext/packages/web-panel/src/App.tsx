import { Suspense, useContext, useEffect, useMemo, useState } from 'react'

import './App.css'
import 'allotment/dist/style.css'

import { VSCodeLink } from '@vscode/webview-ui-toolkit/react'
import { useAtom, useSetAtom } from 'jotai'
import { DevTools } from 'jotai-devtools'
import { FlaskConical, FlaskConicalOff } from 'lucide-react'
import { EventListener } from './baml_wasm_web/EventListener'
import { Button } from './components/ui/button'
import { Dialog, DialogContent, DialogHeader, DialogTitle, DialogTrigger } from './components/ui/dialog'
import { Separator } from './components/ui/separator'
// import { ASTContext, ASTProvider } from './shared/ASTProvider'
import FunctionPanel from './shared/FunctionPanel'
import { ProjectToggle } from './shared/ProjectPanel'
import { FunctionSelector } from './shared/Selectors'
import SettingsDialog, { ShowSettingsButton, showSettingsAtom } from './shared/SettingsDialog'
import CustomErrorBoundary from './utils/ErrorFallback'
import 'jotai-devtools/styles.css'
import { SettingsIcon } from 'lucide-react'
import { showTestsAtom } from './baml_wasm_web/test_uis/testHooks'

const TestToggle = () => {
  // const { setSelection } = useContext(ASTContext)
  const [showTests, setShowTests] = useAtom(showTestsAtom)

  return (
    <Button
      variant='outline'
      className='p-1 text-xs w-fit h-4 border-vscode-textSeparator-foreground'
      onClick={() => setShowTests((prev) => !prev)}
    >
      {showTests ? 'Hide tests' : 'Show tests'}
    </Button>
  )
}

function App() {
  const setShowSettings = useSetAtom(showSettingsAtom)
  return (
    <CustomErrorBoundary>
      <DevTools />
      <Suspense fallback={<div>Loading...</div>}>
        <EventListener>
          <div className='absolute z-10 flex flex-row items-end gap-1 right-1 top-2 text-end'>
            <TestToggle />
            <VSCodeLink href='https://docs.boundaryml.com'>Docs</VSCodeLink>
            <Button className='h-4' onClick={() => setShowSettings(true)}>
              <SettingsIcon className='h-4' />
            </Button>
            <ShowSettingsButton />
          </div>
          <SettingsDialog />
          <div className='flex flex-col gap-2 px-2 pb-4'>
            <FunctionSelector />
            <Separator className='bg-vscode-textSeparator-foreground' />
            <FunctionPanel />
          </div>
        </EventListener>
      </Suspense>
    </CustomErrorBoundary>
  )
}

export default App
