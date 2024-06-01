import { Editor } from '@monaco-editor/react';
import { Alert, Button, CircularProgress } from '@mui/material';
import { useState } from 'react';
import { submitCode, testCode } from './lib/repo';

const App = () => {
  const [code, setCode] = useState<string | undefined>('print("hello world!")');

  return (
    <div className='flex h-screen min-h-screen w-screen flex-col items-center bg-zinc-900 p-32 text-zinc-100'>
      <div className='flex h-full w-[70rem] flex-col gap-8'>
        <div className='flex justify-between'>
          <h1 className='text-4xl text-zinc-100'>Python 3 Online IDE</h1>
          <div className='flex gap-6'>
            <Button variant='contained'
              onClick={() => testCode(code || "")}
            >Test code</Button>

            <Button variant='contained'
              onClick={() => submitCode(code || "")}
            >Submit</Button>
          </div>
        </div>

        <div className='flex flex-1 rounded-2xl border border-zinc-400 p-1'>
          <div className='w-3/5'>
            <Editor
              defaultLanguage='python'
              height={'100%'}
              theme='vs-dark'
              loading={<CircularProgress />}
              value={code}
              onChange={(str) => setCode(str)}
            />
          </div>

          <div className='w-2/5 p-4'>
            <Alert variant="outlined" severity="error">
              <p className='text-red-300'>
                Your code returned an error
              </p>
            </Alert>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
