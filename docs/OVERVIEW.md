# Overview

This file provides a quick overview of the application.

## Functionalities

The application has two functionalities, testing Python code and submitting
Python code. Both go through the same code execution environment in a separate
docker container with restricted access, with the available Docker image Python
3.11 and numpy, pandas, scipy installed. Each process runs in its own container,
and the container is removed right after the code is done executing.

The submission functionality persists the data in a local SQLite database if the
code ran successfully with no std error, in a table named `submissions` with the
following schema

```sql
CREATE TABLE IF NOT EXISTS submissions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT NOT NULL,
    timestamp TEXT NOT NULL
);
```

Repeated submission is prevented through the frontend, where if the user is
currently awaiting for a code execution result, no further submissions are
allowed.

## Code Result

The a code execution result is given back by the backend and displayed on the
frontend, the model is as follow:

```typescript
export type Status = 'success' | 'error';

export type CodeResult = {
  status: Status;
  timestamp: string;
  stdout?: string;
  stderr?: string;
  timeRan?: number;
  message?: string;
};
```

The frontend displays the code output and additional information accordingly.
`message` is an additional field to display any messages from the server that is
not part of the code output, in our case, if a process runs for longer than 10
seconds, it is killed and a message about the timeout is displayed.

## Safety Precautions

A few safety precautions prevent the user from doing SQL injections, infinitely
draining resources and touching the host machine's file system. The specifics
can be found it
[SAFETY.md](https://github.com/SamZhang02/code-editor/blob/main/docs/SAFETY.md)
