const path = require("path");
const VueLoaderPlugin = require("vue-loader/lib/plugin");

module.exports = {
    entry: {
        "dist/main": [path.resolve(__dirname, "src", "index.js")]
    },
    output: {
        path: path.resolve(__dirname),
        filename: "[name].js"
    },
    resolve: {
        extensions: [".vue", ".ts", ".tsx", ".js", ".jsx", ".json", ".css"],
        alias: {
            vue: "vue/dist/vue.js"
        }
    },
    mode: "development",
    module: {
        rules: [{
            test: /\.jsx?$/, // 拡張子がjsxで
            exclude: /node_modules/, // node_modulesフォルダ配下でなければ
            use: [{
                loader: "babel-loader" // babel-loaderを使って変換する
            }]
        },
        {
            test: /\.tsx?$/,
            exclude: /node_modules/,
            use: [{ loader: "ts-loader" }]
        },
        {
            test: /\.css$/,
            use: [
                "vue-style-loader",
                "css-loader"
            ]
        },
        {
            test: /\.vue$/,
            exclude: /node_modules/,
            use: [{ loader: "vue-loader" }]
        }
        ]
    },
    plugins: [new VueLoaderPlugin()],
    devtool: "inline-source-map"
};