import { Alert } from '@mui/material';

import { CodeResult } from '../models/CodeResult';

type CodeOutputProps = {
  type: 'test' | 'submit';
  result: CodeResult;
};

export const CodeOutput = ({ type, result }: CodeOutputProps) => {
  return (
    <div className='flex max-w-full flex-col gap-4 '>
      {result.status === 'success' ? (
        <Alert variant='outlined' severity='success' className='mt-2'>
          <p className='text-green-200'>
            {type === 'test'
              ? 'Your code was successfully executed'
              : 'Your code was successfully executed and stored'}
          </p>
        </Alert>
      ) : (
        <Alert variant='outlined' severity='error'>
          <p className='text-red-300'>Your code returned an error</p>
        </Alert>
      )}

      {result && (
        <div className='flex flex-col gap-4 whitespace-pre-wrap break-words'>
          {result.stdout && (
            <div>
              <p className='font-semibold'>stdout:</p>
              <p>{result.stdout}</p>
            </div>
          )}

          {result.stderr && (
            <div>
              <p className='font-semibold'>stderr:</p>
              <p>{result.stderr}</p>
            </div>
          )}

          <div>
            <p className='text-zinc-500'>
              Code ran in {result.time_ran}ms at {result.timestamp}
            </p>
          </div>
        </div>
      )}
    </div>
  );
};
