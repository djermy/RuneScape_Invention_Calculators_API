// store
import api from '.';
import { Item } from 'store/model';

export const itemApi = api.injectEndpoints({
  endpoints: (builder) => ({
    getAllItem: builder.query<Item[], void>({
      query: () => '/items',
      providesTags: ['Items'],
      keepUnusedDataFor: 0,
    }),
  }),
});

export const { useGetAllItemQuery } = itemApi;

export default itemApi;
