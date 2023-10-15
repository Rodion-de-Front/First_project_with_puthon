import React from "react"
import * as ReactDOMClient from 'react-dom/client';

import "./css/main.css"

import App from "./App"


const app = ReactDOMClient.createRoot(document.getElementById ("app"))

app.render(<App />)