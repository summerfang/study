import React, { Component, Fragment } from "react";
import axios from "axios";
import { Badge } from "react-bootstrap";

class Post extends Component {
    state = { post: null };

    componentDidMount() {
        // ;
        axios
            .get(
                "https://baconipsum.com/api/?type=meat-and-filler¶s=4&format=text"
            )
            .then((response) =>
                this.setState({ post: response.data })
            );
    }

    render() {
        return (
            <Fragment>
                {this.state.post && (
                    <div className="position-relative">
                        <span className="d-block pb-2 mb-0 h6 
                                        text-uppercase text-info 
                                        font-weight-bold">
                            What is the True Up
                            <Badge
                                pill
                                color="success"
                                className="text-uppercase px-2 py-1 
                                            ml-3 mb-1 align-middle"
                                style={{
                                    fontSize: "0.75rem",
                                }}
                            >
                                New
                            </Badge>
                        </span>

                        <span className="d-block pb-4 h2 text-dark 
                                        border-bottom border-gray">
                            Why true up is more important than new logo
                        </span>

                        <article
                            className="pt-5 text-secondary text-justify"
                            style={{
                                fontSize: "0.9rem",
                                whiteSpace: "pre-line",
                            }}
                        >
                            <h1>What is True Up? </h1>

                            True up is a sales strategy that focuses on increasing the revenue from your existing customers by selling them more products or services that match their needs and goals. True up can take various forms, such as upselling, cross-selling, renewing, or expanding contracts, depending on the type and stage of your customer relationship. True up is a win-win situation for both you and your customers, as you can increase your revenue and retention, while your customers can get more value and satisfaction from your products or services.

                            <h1>Why is True Up Ignored? </h1>
                            <p>Many salespeople or business owners tend to overlook or neglect true up, because they are more focused on acquiring new customers, or because they lack the skills or tools to identify and pursue true up opportunities. Some of the common reasons why true up is ignored are:

                                <li>Lack of customer data: Without knowing how your customers are using your products or services, what their pain points or goals are, or how satisfied they are, you cannot tailor your true up offers to their specific needs and preferences. </li>

                                <li>Lack of communication: Without maintaining regular and meaningful contact with your customers, you cannot build trust and rapport, or uncover their challenges or aspirations, or educate them about the benefits of your additional products or services.
                                </li>
                                <li>Lack of incentives: Without aligning your compensation or reward system with your true up goals, you cannot motivate your sales team to pursue true up opportunities, or measure and celebrate their success.
                                </li></p>

                            <h1>Why is True Up Easier and More Cost-Effective? </h1>

                            True up is easier and more cost-effective than acquiring new customers, because you already have an established relationship and trust with your existing customers, and you can leverage your existing knowledge and data about them to create more relevant and personalized offers. Some of the advantages of true up are:

                            <li>Lower acquisition cost: It costs much less to sell to an existing customer than to a new one, as you can save on marketing, advertising, or prospecting expenses.
                            </li>
                            <li>Higher conversion rate: It is much easier to convince an existing customer to buy more from you than to persuade a new one to buy from you for the first time, as you can rely on your proven track record and reputation.
                            </li>
                            <li>Higher lifetime value: It is much more profitable to retain and grow an existing customer than to replace a lost one, as you can increase their loyalty and referrals, and reduce your churn and attrition rates.
                            </li>
                            <h1>What Kind of Data is Needed to Boost True Up? </h1>

                            To boost your true up sales, you need to collect and analyze data that can help you understand your customers better, and identify and act on true up opportunities. Some of the data that you need are:

                            <li>Product usage data: This data can show you how your customers are using your products or services, how often, how much, and for what purposes. You can use this data to segment your customers based on their usage patterns, and target them with relevant offers to increase their usage, upgrade their plans, or cross-sell them complementary products or services.
                            </li>
                            <li>Customer feedback data: This data can show you how your customers feel about your products or services, how satisfied or dissatisfied they are, and what they like or dislike. You can use this data to improve your products or services, address your customers' pain points or complaints, or upsell them features or benefits that can enhance their satisfaction or solve their problems.
                            </li>
                        </article>
                    </div>
                )}
            </Fragment>
        );
    }
}

export default Post;