import { createRouter, createWebHistory } from "vue-router";

import HomePage from "@/pages/home/HomePage.vue";
import NotFoundPage from "@/pages/NotFoundPage.vue";
import PaymentsPage from "@/pages/payments/PaymentPage.vue";

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: "/",
            name: "Home",
            component: HomePage,
        },
        {
            path: "/payments",
            name: "Payments",
            component: PaymentsPage,
        },
        {
            path: "/products",
            name: "Products",
            component: () => import("@/pages/products/ProductsPage.vue"),
        },
        {
            path: "/products/:id",
            name: "ProductDetail",
            component: () =>
                import("@/pages/products/details/ProductDetail.vue"),
        },
        {
            path: "/about",
            name: "About",
            component: () => import("../pages/AboutPage.vue"),
        },
        {
            path: "/404",
            name: "404",
            meta: { noAuth: true },
            component: NotFoundPage,
        },
        // will match everything and put it under `route.params.pathMatch`
        {
            path: "/:pathMatch(.*)*",
            redirect: { name: "404" },
            meta: { noAuth: true },
        },
    ],
    scrollBehavior(to, from, savedPosition) {
        if (to.hash) {
            return {
                el: to.hash,
                behavior: "smooth",
                top: 200,
            };
        }

        // return to top
        return { top: 0, behavior: "smooth" };
    },
});

export default router;
