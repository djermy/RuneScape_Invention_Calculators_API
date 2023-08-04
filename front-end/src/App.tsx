// react
import React, { memo, useState, useMemo } from 'react';
import styled from '@emotion/styled';

// style
import { GlobalStyle } from 'GlobalStyle';

// components
import { Navbar } from 'components/Navbar';
import { RsItem } from 'components/RsItem';

// mui
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { Container, TextField } from '@mui/material';
import { FixedSizeList, areEqual } from 'react-window';

// store
import { useGetAllItemQuery } from 'store/api/item';

const theme = createTheme({
  palette: {
    mode: 'dark',
  },
});

const Row = memo(({ data, index, style }: any) => {
  // Data passed to List as "itemData" is available as props.data
  const item = data[index];

  return <RsItem item={item} style={style} />;
}, areEqual);

const App = () => {
  // state
  const [search, setSearch] = useState('');

  // hooks
  const items = useGetAllItemQuery();

  // memos
  const filteredItems = useMemo(() => {
    if (!items || !items.data) return [];
    return items.data.filter((item) =>
      item.name.toLowerCase().includes(search.toLowerCase()),
    );
  }, [items, search]);

  return (
    <ThemeProvider theme={theme}>
      <GlobalStyle />
      <Wrapper>
        <Navbar />
        <Container>
          <TextField
            id='outlined-basic'
            style={{ marginBottom: 32, width: '100%' }}
            label='Search'
            variant='outlined'
            value={search}
            onChange={(e) => setSearch(e.target.value)}
          />
          {filteredItems && (
            <StyledFixedSizeList
              height={800}
              itemSize={110}
              itemCount={filteredItems.length}
              itemData={filteredItems}
              width='100%'
              overscanCount={30}
            >
              {Row}
            </StyledFixedSizeList>
          )}
        </Container>
      </Wrapper>
    </ThemeProvider>
  );
};

const Wrapper = styled.div`
  display: flex;
  flex-direction: column;
  gap: 32px;
`;

const StyledFixedSizeList = styled(FixedSizeList)`
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 16px;

  /* width */
  ::-webkit-scrollbar {
    width: 10px;
  }

  /* Track */
  ::-webkit-scrollbar-track {
    background: #555;
  }

  /* Handle */
  ::-webkit-scrollbar-thumb {
    background: #888;
  }

  /* Handle on hover */
  ::-webkit-scrollbar-thumb:hover {
    background: #aaa;
  }
`;

export default App;
