const path = require('path');
const webpack = require('webpack');

module.exports = {
  entry: './config/static/src/index.js',
  output: {
    path: path.resolve(__dirname, 'config/static/dist'),
    filename: 'bundle.js',
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: ['@babel/preset-env'],
          },
        },
      },
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader'],
      },
    ],
  },
  devServer: {
    static: {
      directory: path.join(__dirname, 'config/static/dist'),
    },
    compress: true,
    port: 9000,
    hot: true,
    headers: {
      'Access-Control-Allow-Origin': '*',
    },
    devMiddleware: {
      publicPath: '/static/dist/',
    },
  },
  plugins: [
    new webpack.HotModuleReplacementPlugin(),
  ],
};
