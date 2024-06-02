import { Editor } from '@monaco-editor/react';
import { Button, CircularProgress } from '@mui/material';
import { useState } from 'react';

import { CodeOutput } from './components/CodeOutput';
import { submitCode, testCode } from './lib/api';
import { CodeResult } from './models/CodeResult';

const App = () => {
  const [code, setCode] = useState<string>('print("hello world!")');
  const [outputType, setOutputType] = useState<'test' | 'submit'>('test');
  const [waitingForOutput, setWaitingForOutPut] = useState<boolean>(false);
  const [result, setResult] = useState<CodeResult | null>(null);

  const handleTestCode = async () => {
    if (!waitingForOutput) {
      setWaitingForOutPut(true);
      const result = await testCode(code);
      setWaitingForOutPut(false);
      setResult(result);
      setOutputType('test');
    }
  };
  const handleSubmitCode = async () => {
    if (!waitingForOutput) {
      setWaitingForOutPut(true);
      const result = await submitCode(code);
      setWaitingForOutPut(false);
      setResult(result);
      setOutputType('submit');
    }
  };

  return (
    <div className='flex h-screen min-h-screen w-screen flex-col items-center bg-zinc-900 p-32 text-zinc-100'>
      <div className='flex h-full w-[70rem] flex-col gap-8'>
        <div className='flex justify-between'>
          <h1 className='text-4xl text-zinc-100'>Python 3 Online</h1>
          <div className='flex gap-6'>
            <Button variant='contained' onClick={handleTestCode}>
              Test code
            </Button>

            <Button variant='contained' onClick={handleSubmitCode}>
              Submit
            </Button>
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
              onChange={(str) => setCode(str || '')}
            />
          </div>

          <div className='w-2/5 p-4 flex'>
            {waitingForOutput ? (
              <CircularProgress className='mx-auto my-auto'/>
            ) : (
              result && <CodeOutput result={result} type={outputType} />
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default App;
