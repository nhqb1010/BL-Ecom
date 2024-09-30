function capitalizeString(str: string): string {
    return str.charAt(0).toUpperCase() + str.slice(1);
}

function transformToVNDFormat(price: number): string {
    return price.toLocaleString("it-IT", {
        style: "currency",
        currency: "VND",
    });
}

function getValue(key: string, obj: Object, defaultValue?: any): any {
    return obj.hasOwnProperty(key)
        ? obj[key as keyof object]
        : defaultValue !== undefined
        ? defaultValue
        : undefined;
}

export { capitalizeString, getValue, transformToVNDFormat };
