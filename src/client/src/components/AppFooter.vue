<script setup lang="ts">
import Social from "./Social.vue";
</script>

<template>
    <footer id="footer">
        <div class="footer__container">
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

            <!-- Social Links -->
            <div class="footer-box social">
                <!-- Icon -->
                <!-- Basket Icon -->
                <RouterLink :to="{ name: 'Home' }" class="nav__logo">
                    <i class="bx bx-basket"></i>Delicacy
                </RouterLink>

                <!-- Address -->
                <p>
                    Số X, đường Y, khu dân cư Hưng Phú 1, phường Hưng Phú, Quận
                    Cái Răng
                </p>

                <!-- Social -->
                <Social class="social__container" />
            </div>
        </div>
    </footer>
</template>

<style lang="scss">
footer {
    background-color: #fef4ea;

    .footer__container {
        max-width: 1340px;
        margin-inline: auto;
        margin-top: 2rem;
        padding: 2rem;

        display: grid;
        gap: 2rem;

        border-radius: 0.5rem;

        .footer-box {
            display: flex;
            flex-direction: column;
            line-height: 2;

            h2 {
                font-size: 1.1rem;
                font-weight: 600;
                margin-bottom: 1rem;
            }

            p {
                font-size: 0.938rem;
                margin: 0.5rem 0 1rem;
            }

            a {
                color: rgb(75, 74, 74);
                transition: all 0.1s ease-in;

                &:hover {
                    color: var(--green-color);
                    text-decoration: underline;
                }
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

            &.social {
                margin-top: 2rem;
                max-width: 60ch;

                .nav__logo {
                    font-size: 1.8rem;
                    color: var(--orange-color);

                    i {
                        font-size: 2.2rem;
                    }
                }
            }
        }
    }
}

@media screen and (min-width: 720px) {
    footer {
        .footer__container {
            padding: 3rem;
            grid-template-columns: 1fr 1fr;
        }
    }
}

@media screen and (min-width: 968px) {
    footer {
        .footer__container {
            padding: 3rem;

            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));

            .footer-box {
                &.social {
                    margin-top: initial;

                    .nav__logo {
                        font-size: 1.5rem;

                        i {
                            font-size: 2rem;
                        }
                    }
                }
            }
        }
    }
}
</style>
