//インライン化されたhtmlをビルドするための設定ファイル
import { resolve } from "path";
import { defineConfig } from "vite";
import { viteSingleFile } from "vite-plugin-singlefile";

const root = resolve(__dirname, "02_tmp_html");
const outDir = resolve(__dirname, "03_output_html");

export default defineConfig({
  root,

  build: {
    outDir: outDir,
    emptyOutDir: false, //mdや.gitignoreを消さない
  },

  plugins: [viteSingleFile()], // This is the plugin 😃

  // base: process.env.GITHUB_PAGES ? "REPOSITORY_NAME" : "./",
});
