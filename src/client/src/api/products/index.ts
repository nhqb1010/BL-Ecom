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
        description:
            "Nâng tầm vị giác cùng sức hấp dẫn tinh tế của hạt điều được pha trộn tinh tế với phố mai êm dịu, mỗi miếng cắn mang đến một vũ điệu tinh tế tao nền một trải nghiệm giác quan khó quên.",
    },
    {
        id: "uuid-1003",
        imageUrl: productImgUrl2.default,
        name: "OR'SHOW CHOCO",
        price: 90_000,
        categories: "bag",
        description:
            "Hạt điều và socola? Tại sao không! Một sự kết hợp mang đến cho bạn trải nghiệm ăn vặt đầy bất ngờ. Với độ bùi của hạt điều Or'Show được phủ một lớp sốt socola thơm ngon, sẽ khiến bạn mê mẫn với lần thử đầu tiên.",
    },
    {
        id: "uuid-1002",
        imageUrl: productImgUrl3.default,
        name: "OR'SHOW APRICOT",
        price: 70_000,
        categories: "bag",
        description:
            "Nâng tầm vị giác cùng sức hấp dẫn tinh tế của hạt điều được pha trộn tinh tế với phố mai êm dịu, mỗi miếng cắn mang đến một vũ điệu tinh tế tạo nên một trải nghiệm giác quan khó quên.",
    },
    {
        id: "uuid-1001",
        imageUrl: productImgUrl4.default,
        name: "OR'SHOW BƠ",
        price: 100_000,
        categories: "bag",
        description:
            "Phủ lên mình lớp bơ đường óng ả, hạt điều bơ Or'Show sẽ khiến bạn muốn thưởng thức lại sau lần thử đầu tiến! Với vị ngọt thanh của bơ và độ bùi của hạt điều Or'Show chắc chắn sẽ đem lại cho bạn một trải nghiệm ấn tượng.",
    },
    {
        id: "uuid-1000",
        imageUrl: productImgUrl5.default,
        name: "OR'SHOW TỎI ỚT",
        price: 95_000,
        categories: "bag",
        description:
            "Tìm kiếm hương vị đậm đà để ăn vặt khi buồn miệng? Hạt điều tỏi ớt Or'Show sẽ làm bạn hài lòng! Được nếm nếm kỹ lưỡng với hương vị tỏi và ớt, hạt điều tỏi ớt Or'Show đem đến vị đậm đà lôi cuốn không thể ngừng. Thử ngay hạt điều tỏi ớt Or'Show - đậm vị không thể cưỡng lại!",
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

export const getProductById = async (
    id: any
): Promise<IProductDetailType | null> => {
    // return new Promise((resolve) => {
    //     setTimeout(() => {
    //         resolve(mockData.find((product) => product.id === id) || null);
    //     }, 1000);
    // });

    return mockData.find((product) => product.id === id) || null;
};
