import type { IProductDetailType } from "@/types/products";

const mockData: IProductDetailType[] = [
    {
        id: "uuid-100",
        imageUrl: "https://picsum.photos/159/300",
        name: "Laptop Dell XPS 13 9310",
        price: 40000000,
        originalPrice: 45000000,
        categories: "Laptop",
    },
    {
        id: "uuid-101",
        imageUrl: "https://picsum.photos/150/300",
        name: "Tai nghe không dây Sony WH-1000XM4",
        price: 8000000,
        categories: "Tai nghe",
    },
    {
        id: "uuid-102",
        imageUrl: "https://picsum.photos/151/300",
        name: "Samsung Galaxy Buds FE",
        price: 3_500_000,
        categories: "Tai nghe",
    },
    {
        id: "uuid-103",
        imageUrl: "https://picsum.photos/152/300",
        name: "Bàn phím cơ Corsair K95 RGB Platinum XT",
        price: 5000000,
        categories: "Phụ kiện máy tính",
    },
    {
        id: "uuid-104",
        imageUrl: "https://picsum.photos/153/300",
        name: "Máy in laser đa chức năng HP LaserJet Pro MFP M428fdw",
        price: 15000000,
        categories: "Phụ kiện máy tính",
    },
    {
        id: "uuid-105",
        imageUrl: "https://picsum.photos/154/300",
        name: "Màn hình cong Samsung Odyssey G7 27 inch",
        price: 18000000,
        categories: "Phụ kiện máy tính",
    },
    {
        id: "uuid-106",
        imageUrl: "https://picsum.photos/155/300",
        name: "Ổ cứng di động SSD Samsung T7 1TB",
        price: 3000000,
        categories: "Phụ kiện máy tính",
    },
    {
        id: "uuid-107",
        imageUrl: "https://picsum.photos/156/300",
        name: "Máy sấy tóc Dyson Supersonic",
        price: 9000000,
        categories: "Phụ kiện máy tính",
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
