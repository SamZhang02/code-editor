export type Status = 'success' | 'error';

export type CodeResult = {
  status: Status;
  stdout?: string;
  stderr?: string;
  timeRan?: number;
  timestamp: string;
};
