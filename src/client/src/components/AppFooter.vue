<script setup lang="ts">
import Social from "./Social.vue";
</script>

<template>
    <footer id="footer">
        <div class="footer-box">
            <!-- Icon -->
            <!-- Basket Icon -->
            <RouterLink :to="{ name: 'Home' }" class="nav__logo">
                <i class="bx bx-basket"></i>Delicacy
            </RouterLink>

            <!-- Address -->
            <p>
                Số X, đường Y, khu dân cư Hưng Phú 1, phường Hưng Phú, Quận Cái
                Răng
            </p>

            <!-- Social -->
            <Social class="social__container" />
        </div>

        <!-- About-Us Sections -->
        <div class="footer-box">
            <h3>Về PMBL-shee</h3>

            <ul class="box-links">
                <li>
                    <!-- <RouterLink :to="{ name: 'About' }">
                            Về Chúng Tôi
                        </RouterLink> -->

                    <a href="#">Về Chúng Tôi</a>
                </li>
                <li>
                    <!-- <RouterLink :to="{ name: 'Contact' }">
                            Liên Hệ
                        </RouterLink> -->

                    <a href="#">Liên Hệ</a>
                </li>
            </ul>
        </div>

        <!-- Payment Section -->
        <div class="footer-box">
            <h3>Thanh Toán</h3>

            <ul class="box-links">
                <li>
                    <a href="#">Hướng Dẫn Thanh Toán</a>
                </li>
                <li>
                    <a href="#">Phương Thức Thanh Toán</a>
                </li>
            </ul>
        </div>
    </footer>
</template>

<style lang="scss">
footer {
    max-width: 968px;
    margin-inline: auto;
    margin-top: 2rem;
    padding: 20px;

    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1.5rem;

    background-color: #fef4ea;
    border-radius: 0.5rem;

    .footer-box {
        display: flex;
        flex-direction: column;

        h2 {
            font-size: 1.1rem;
            font-weight: 600;
            margin-bottom: 1rem;
        }

        p {
            font-size: 0.938rem;
            margin: 0.5rem 0 1rem;
        }

        .social__container {
            display: flex;
            align-items: center;
            gap: 0.5rem;

            .social-link {
                i {
                    padding: 10px;
                    background-color: var(--bg-color);
                    color: var(--green-color);
                    border-radius: 5rem;
                    font-size: 20px;
                    transition: all 0.2s linear;
                }

                &:hover {
                    i {
                        background-color: var(--green-color);
                        color: var(--bg-color);
                    }
                }
            }
        }
    }
}
</style>
