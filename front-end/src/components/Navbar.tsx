// react
import React from 'react';

// mui
import { AppBar, Toolbar, Typography, Container } from '@mui/material';

export const Navbar = () => {
  return (
    <AppBar position='static'>
      <Toolbar>
        <Container>
          <Typography variant='h5'>Runescape Calculator</Typography>
        </Container>
      </Toolbar>
    </AppBar>
  );
};

Navbar.displayName = 'Navbar';
export default Navbar;
