import type { IProductDetailType } from "@/types/products";

import * as productImgUrl1 from "@/assets/images/products/1.png";
import * as productImgUrl2 from "@/assets/images/products/2.png";
import * as productImgUrl3 from "@/assets/images/products/3.png";
import * as productImgUrl4 from "@/assets/images/products/4.png";
import * as productImgUrl5 from "@/assets/images/products/5.png";

const mockData: IProductDetailType[] = [
    {
        id: "uuid-1004",
        imageUrl: productImgUrl1.default,
        name: "OR'SHOW PHÔ MAI",
        price: 50_000,
        categories: "bag",
    },
    {
        id: "uuid-1003",
        imageUrl: productImgUrl2.default,
        name: "OR'SHOW CHOCO",
        price: 90_000,
        categories: "bag",
    },
    {
        id: "uuid-1002",
        imageUrl: productImgUrl3.default,
        name: "OR'SHOW APRICOT",
        price: 70_000,
        categories: "bag",
    },
    {
        id: "uuid-1001",
        imageUrl: productImgUrl4.default,
        name: "OR'SHOW BƠ",
        price: 100_000,
        categories: "bag",
    },
    {
        id: "uuid-1000",
        imageUrl: productImgUrl5.default,
        name: "OR'SHOW TỎI ỚT",
        price: 95_000,
        categories: "bag",
    },
    {
        id: "uuid-101",
        imageUrl: "https://picsum.photos/150/300",
        name: "Tai nghe không dây Sony WH-1000XM4",
        price: 800_0000,
        categories: "Tai nghe",
    },
    {
        id: "uuid-102",
        imageUrl: "https://picsum.photos/151/300",
        name: "Samsung Galaxy Buds FE",
        price: 3_500_000,
        categories: "Tai nghe",
    },
];

export const getProducts = async (): Promise<IProductDetailType[]> => {
    // return new Promise((resolve) => {
    //     setTimeout(() => {
    //         resolve(mockData);
    //     }, 1000);
    // });

    return mockData;
};

export const filterProductsByCategory = async (
    category: string
): Promise<IProductDetailType[]> => {
    // return new Promise((resolve) => {
    //     setTimeout(() => {
    //         resolve(mockData.filter((product) => product.categories === category));
    //     }, 1000);
    // });

    return mockData.filter((product) => product.categories === category);
};

export const sortProductsByPrice = async (
    products: IProductDetailType[],
    order: "asc" | "desc"
): Promise<IProductDetailType[]> => {
    // return new Promise((resolve) => {
    //     setTimeout(() => {
    //         resolve(
    //             products.sort((a, b) =>
    //                 order === "asc" ? a.price - b.price : b.price - a.price
    //             )
    //         );
    //     }, 1000);
    // });

    const data = [...products];

    return data.sort((a, b) =>
        order === "asc" ? a.price - b.price : b.price - a.price
    );
};
