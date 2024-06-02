export type Status = 'success' | 'error';

export type CodeResult = {
  status: Status;
  timestamp: string;
  stdout?: string;
  stderr?: string;
  timeRan?: number;
  message?: string;
};
