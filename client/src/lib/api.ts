import { CodeResult } from '../models/CodeResult';

const serverUrl = import.meta.env.VITE_SERVER_URL || "http://127.0.0.1:8000/";

const prefix = 'api';

const post = async <T, U>(url: string, data: T): Promise<U> => {
  try {
    const response = await fetch(serverUrl + prefix + url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    });

    if (!response.ok) {
      const errorText = await response.text();
      throw new Error(`Error ${response.status}: ${errorText}`);
    }

    return (await response.json()) as U;
  } catch (error) {
    console.error('Error making POST request:', error);
    throw error;
  }
};

export const testCode = async (code: string): Promise<CodeResult> => {
  return post('/code/test', { code });
};

export const submitCode = async (code: string): Promise<CodeResult> => {
  return post('/code/submit', { code });
};
