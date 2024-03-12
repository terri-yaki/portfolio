import { createTheme } from '@mui/material/styles';

const theme = createTheme({
 palette: {
    primary: {
      main: '#1976d2',
    },
    secondary: {
      main: '#dc004e',
    },
 },
 typography: {
    fontFamily: 'Roboto, sans-serif',
    fontSize: 14,
    fontWeightLight: 300,
    fontWeightRegular: 400,
    fontWeightMedium: 500,
    fontWeightBold: 700,
 },
});

export default theme;