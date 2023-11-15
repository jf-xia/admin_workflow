import React from "react";
import { createRoot } from "react-dom/client";

import App from "./App";
import "./i18n";

const container = document.getElementById("root") as HTMLElement;
const root = createRoot(container);

import { QueryClient, useQuery, QueryClientProvider } from "@tanstack/react-query";

const queryClient = new QueryClient();

root.render(
  <React.StrictMode>
    <React.Suspense fallback="loading">
      <QueryClientProvider client={queryClient}>
        <App />
      </QueryClientProvider>
    </React.Suspense>
  </React.StrictMode>
);
