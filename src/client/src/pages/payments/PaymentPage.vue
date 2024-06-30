<script setup lang="ts">
import { onMounted, ref } from "vue";
import { useRoute } from "vue-router";

import Accordion from "primevue/accordion";
import AccordionContent from "primevue/accordioncontent";
import AccordionHeader from "primevue/accordionheader";
import AccordionPanel from "primevue/accordionpanel";

enum PaymentMethod {
    CASH = "cash",
    BANK_TRANSFER = "bank_transfer",
    MOMO = "momo",
}

const route = useRoute();

const activePayments = ref<PaymentMethod[]>([]);

onMounted(() => {
    // If hash exists, set activePayments to the hash value
    // Else default to BANK_TRANSFER
    let hash = route.hash;
    if (hash) {
        hash = hash.replace("#", "");

        if (Object.values(PaymentMethod).includes(hash as PaymentMethod)) {
            activePayments.value = [hash as PaymentMethod];
        }
    } else {
        activePayments.value = [PaymentMethod.BANK_TRANSFER];
    }
});
</script>

<template>
    <section class="payments payments__container">
        <!-- Title -->
        <h2 class="payments__title">Phương Thức Thanh Toán</h2>

        <!-- Payments -->
        <Accordion
            class="payment-methods__container"
            :value="activePayments"
            multiple
        >
            <!-- Bank Transfer -->
            <AccordionPanel
                class="method-container"
                :value="PaymentMethod.BANK_TRANSFER"
                :id="PaymentMethod.BANK_TRANSFER"
            >
                <AccordionHeader>Chuyển Khoản Ngân Hàng</AccordionHeader>
                <AccordionContent>
                    <p>
                        Chúng tôi sẽ thu tiền trước 100% giá trị đơn hàng + phí
                        vận chuyển theo cước phí tính trong chinh sách vận
                        chuyển bằng phương thức chuyển khoản trước khi giao
                        hàng. Quý khách chuyển tiền cho chúng tôi vào tài khoản
                        Cty sau đây:
                    </p>
                    <p><span class="header">CÔNG TY:</span> XXXX</p>
                    <p><span class="header">Đại diện:</span> PMLBL</p>
                    <p><span class="header">Tài khoản:</span> 42410000336333</p>
                    <p><span class="header">Ngân hàng:</span> Sacombank</p>
                </AccordionContent>
            </AccordionPanel>

            <!-- Cash -->
            <AccordionPanel
                :value="PaymentMethod.CASH"
                :id="PaymentMethod.CASH"
            >
                <AccordionHeader>Thanh Toán Khi Nhận Hàng</AccordionHeader>
                <AccordionContent>
                    <p>
                        Quý khách thanh toán cho nhân viên giao nhận toàn bộ
                        hoặc phần còn lại của giá trị đơn hàng đã mua. Hình thức
                        thanh toán này chỉ thực hiện với các đơn hàng có địa chỉ
                        giao hàng tại Hà Nội. Nếu địa điểm giao hàng ngay tại
                        nơi thanh toán, nhân viên giao hàng của chúng tôi sẽ thu
                        tiền khi giao hàng.
                    </p>
                </AccordionContent>
            </AccordionPanel>

            <!-- Momo -->
            <AccordionPanel
                :value="PaymentMethod.MOMO"
                :id="PaymentMethod.MOMO"
            >
                <AccordionHeader>Momo</AccordionHeader>
                <AccordionContent>
                    <p class="m-0">
                        At vero eos et accusamus et iusto odio dignissimos
                        ducimus qui blanditiis praesentium voluptatum deleniti
                        atque corrupti quos dolores et quas molestias excepturi
                        sint occaecati cupiditate non provident, similique sunt
                        in culpa qui officia deserunt mollitia animi, id est
                        laborum et dolorum fuga. Et harum quidem rerum facilis
                        est et expedita distinctio. Nam libero tempore, cum
                        soluta nobis est eligendi optio cumque nihil impedit quo
                        minus.
                    </p>
                </AccordionContent>
            </AccordionPanel>
        </Accordion>
    </section>
</template>

<style lang="scss">
.payments {
    margin-top: var(--nav-height);
    margin-inline: auto;
    padding: 1rem 0;

    width: 90% !important;
    max-width: 1000px;

    .payments__title {
        font-size: 2rem;
        font-weight: 600;
        text-align: center;
        margin-block: 1rem;

        @media (min-width: 584px) {
            margin-bottom: 2rem;
        }
    }

    .payment-methods__container {
        --p-accordion-header-active-color: var(--orange-color);
        --p-accordion-header-active-hover-color: var(--orange-color);
        --p-accordion-header-hover-color: var(--light-orange-color);
        // margin-block: 2rem;

        .p-accordionheader {
            font-size: 1.2rem;
            font-weight: 700 !important;
            font-family: var(--vn-font-family);
            padding: 1rem 0;
            cursor: pointer;
            transition: all 0.4s ease;

            &:hover {
                background-color: var(--green-color);
                color: var(--bg-color);
                border-radius: 5rem;
            }
        }

        p {
            font-size: 1.1rem;
            line-height: 1.5;
            margin-bottom: 0.5rem;

            span.header {
                font-weight: 700;
            }
        }
    }
}
</style>
