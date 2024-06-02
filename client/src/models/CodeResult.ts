export type Status = 'success' | 'error';

export type CodeResult = {
  status: Status;
  stdout: string;
  stderr: string;
  time_ran: string;
  timestamp: string;
};
