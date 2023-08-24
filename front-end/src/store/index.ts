// react
import { configureStore, combineReducers } from '@reduxjs/toolkit';
import { localStorageMiddleware, preloadState } from './middleware';
import {
  useSelector as useReduxSelector,
  TypedUseSelectorHook,
} from 'react-redux';

// store
import api from './api';

// reducers
const rootReducer = combineReducers({
  [api.reducerPath]: api.reducer,
});

// create store
const store = configureStore({
  reducer: rootReducer,
  preloadedState: preloadState(),
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware()
      .concat(api.middleware)
      .concat(localStorageMiddleware),
  devTools: process.env.nodeEnv !== 'production',
});

// types
export type RootState = ReturnType<typeof rootReducer>;
export type AppDispatch = typeof store.dispatch;

// hooks
export const useSelector: TypedUseSelectorHook<RootState> = useReduxSelector;

export default store;
