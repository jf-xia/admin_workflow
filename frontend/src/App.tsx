import { Authenticated, GitHubBanner, Refine } from "@refinedev/core";
import { DevtoolsPanel, DevtoolsProvider } from "@refinedev/devtools";
import { RefineKbar, RefineKbarProvider } from "@refinedev/kbar";

import {
  ErrorComponent,
  ThemedLayoutV2,
  ThemedSiderV2,
  ThemedTitleV2,
  useNotificationProvider,
} from "@refinedev/antd";
import "@refinedev/antd/dist/reset.css";

import routerBindings, {
  CatchAllNavigate,
  DocumentTitleHandler,
  NavigateToResource,
  UnsavedChangesNotifier,
} from "@refinedev/react-router-v6";
import dataProvider from "@refinedev/simple-rest";
import { ConfigProvider, App as AntdApp } from "antd";
import { useTranslation } from "react-i18next";
import { BrowserRouter, Outlet, Route, Routes } from "react-router-dom";
import { authProvider } from "./authProvider";
import { Header } from "./components/header";
import { ColorModeContextProvider } from "./contexts/color-mode";
import {
  BlogPostCreate,
  BlogPostEdit,
  BlogPostList,
  BlogPostShow,
} from "./pages/blog-posts";
import {
  CategoryCreate,
  CategoryEdit,
  CategoryList,
  CategoryShow,
} from "./pages/categories";
import {
  EntityCreate,
  EntityEdit,
  EntityList,
  EntityShow,
} from "./pages/entity";
import { ForgotPassword } from "./pages/forgotPassword";
import { Login } from "./pages/login";
import { Register } from "./pages/register";

import { useQuery } from "@tanstack/react-query";

function App() {
  const { t, i18n } = useTranslation();

  const i18nProvider = {
    translate: (key: string, params: object) => t(key, params),
    changeLocale: (lang: string) => i18n.changeLanguage(lang),
    getLocale: () => i18n.language,
  };

  // const {isLoading, error, data} = useQuery(["settings"], () => {
  //   return fetch("http://localhost:7777/api/e/1/").then(res => res.json());
  // });
  // if (isLoading) return <span>Loading...</span>;
  // if (error) {
  //   console.log(error);
  //   return <span>An error has occurred...</span>;
  // }
  // // console.log(data);

  return (
    <BrowserRouter>
      <ConfigProvider>
        <RefineKbarProvider>
          <ColorModeContextProvider>
            <AntdApp>
              <DevtoolsProvider>
                <Refine
                  dataProvider={dataProvider("http://localhost:7777/api/e")}
                  notificationProvider={useNotificationProvider}
                  routerProvider={routerBindings}
                  authProvider={authProvider}
                  i18nProvider={i18nProvider}
                  resources={[
                    {
                      name: "request",
                      list: "/entity",
                      create: "/entity/create",
                      edit: "/entity/edit/:id",
                      show: "/entity/show/:id",
                      meta: {
                        canDelete: true,
                        name: "Entity",
                      },
                    },
                    // {
                    //   name: "categories",
                    //   list: "/categories",
                    //   create: "/categories/create",
                    //   edit: "/categories/edit/:id",
                    //   show: "/categories/show/:id",
                    //   meta: {
                    //     canDelete: true,
                    //   },
                    // },
                  ]}
                  options={{
                    syncWithLocation: true,
                    warnWhenUnsavedChanges: true,
                    projectId: "UIzHbh-q2OfXq-aYEUkV",
                  }}
                >
                  <Routes>
                    <Route
                      element={
                        <Authenticated
                          key="authenticated-inner"
                          fallback={<CatchAllNavigate to="/login" />}
                        >
                          <ThemedLayoutV2
                            Header={() => <Header sticky />}
                            Sider={(props) => (
                              <ThemedSiderV2
                                {...props}
                                Title={() => <ThemedTitleV2 text="Admin T" />}
                                fixed
                              />
                            )}
                          >
                            <Outlet />
                          </ThemedLayoutV2>
                        </Authenticated>
                      }
                    >
                      <Route
                        index
                        element={<NavigateToResource resource="blog_posts" />}
                      />
                      <Route path="/entity">
                        <Route index element={<EntityList />} />
                        <Route path="create" element={<EntityCreate />} />
                        <Route path="edit/:id" element={<EntityEdit />} />
                        <Route path="show/:id" element={<EntityShow />} />
                      </Route>
                      <Route path="/blog-posts">
                        <Route index element={<BlogPostList />} />
                        <Route path="create" element={<BlogPostCreate />} />
                        <Route path="edit/:id" element={<BlogPostEdit />} />
                        <Route path="show/:id" element={<BlogPostShow />} />
                      </Route>
                      <Route path="/categories">
                        <Route index element={<CategoryList />} />
                        <Route path="create" element={<CategoryCreate />} />
                        <Route path="edit/:id" element={<CategoryEdit />} />
                        <Route path="show/:id" element={<CategoryShow />} />
                      </Route>
                      <Route path="*" element={<ErrorComponent />} />
                    </Route>
                    <Route
                      element={
                        <Authenticated
                          key="authenticated-outer"
                          fallback={<Outlet />}
                        >
                          <NavigateToResource />
                        </Authenticated>
                      }
                    >
                      <Route path="/login" element={<Login />} />
                      <Route path="/register" element={<Register />} />
                      <Route
                        path="/forgot-password"
                        element={<ForgotPassword />}
                      />
                    </Route>
                  </Routes>

                  <RefineKbar />
                  <UnsavedChangesNotifier />
                  <DocumentTitleHandler />
                </Refine>
                <DevtoolsPanel />
              </DevtoolsProvider>
            </AntdApp>
          </ColorModeContextProvider>
        </RefineKbarProvider>
      </ConfigProvider>
    </BrowserRouter>
  );
}

export default App;
