// react
import { Middleware } from '@reduxjs/toolkit';
import { RootState } from 'store';

/**
 * localStorage middleware ensures localStorage always has a serialized version
 * of the store. This is useful for persisting state between page refreshes, as
 * well as for implementing an offline-first strategy.
 */
export const localStorageMiddleware: Middleware<{}, RootState> =
  ({ getState }) =>
  (next) =>
  (action) => {
    const result = next(action);
    localStorage.setItem('reduxState', JSON.stringify(getState()));
    return result;
  };

/**
 * preloadState deserializes the store from localStorage and returns it.
 */
export const preloadState = () => {
  try {
    const serializedState = localStorage.getItem('reduxState');
    if (serializedState === null) {
      return undefined;
    }

    let state = JSON.parse(serializedState);
    return state;
  } catch (err) {
    return undefined;
  }
};
