// react
import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';

export const apiUrl = process.env.REACT_APP_API_URL || 'http://localhost:5000';

export const api = createApi({
  reducerPath: 'api',
  baseQuery: fetchBaseQuery({
    baseUrl: `${apiUrl}`,
    credentials: 'include',
  }),
  endpoints: () => ({}),
  tagTypes: ['Items'],
});

export default api;
