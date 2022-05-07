primary_color <- "lightblue"
secondary_color <- "darkblue"
title_size <- 24
axis_font_size <- 16

create_price_diff_hist <- function(df, option_one, option_two) {
    q_10 <- quantile(df$price_diff, .10)
    q_90 <- quantile(df$price_diff, .90)
    iqr <- IQR(df$price_diff)
    indices <- df$price_diff > (q_10 - 1.5 * iqr) &
        df$price_diff < (q_90 + 1.5 * iqr)

    no_outliers <- subset(df, indices)
    ggplot(no_outliers, aes(x = price_diff)) +
        geom_histogram(binwidth = 1, color = secondary_color, fill = primary_color) +# nolint
        ggtitle(paste("Price Difference between", option_one, "and", option_two)) +# nolint
        theme(
            plot.title = element_text(color = secondary_color, size = title_size),
            axis.title.x = element_text(color = secondary_color, size = axis_font_size),
            axis.title.y = element_text(color = secondary_color, size = axis_font_size) # nolint
        ) +
        xlab("Price Difference") +
        ylab("Occurences")
}

create_price_comp_hist <- function(df) {
    q_10 <- quantile(df$price, .10)
    q_90 <- quantile(df$price, .90)
    iqr <- IQR(df$price)
    indices <- df$price > (q_10 - 1.5 * iqr) &
        df$price < (q_90 + 1.5 * iqr)

    no_outliers <- subset(df, indices)
    no_outliers$vegetarian <- ifelse(no_outliers["vegetarian"] == 1, "Yes", "No")
    ggplot(no_outliers, aes(x = price, fill = vegetarian)) +
        geom_histogram(alpha = 0.5, position = "identity", binwidth = 1) +
        ggtitle("Price Distribution of Non-Vegetarian and Vegetarian Recipes") +# nolint
        theme(
            plot.title = element_text(color = secondary_color, size = title_size),
            axis.title.x = element_text(color = secondary_color, size = axis_font_size),
            axis.title.y = element_text(color = secondary_color, size = axis_font_size) # nolint
        ) +
        xlab("Price per Serving") +
        ylab("Occurences") +
        guides(color = "none") + labs(fill = "Vegetarian")
}

create_linear_regression_plot <- function(df) {
    ggplot(df, aes(x = repeats, y = price)) +
        geom_point() +
        geom_smooth(method = lm, se = FALSE) +
        ggtitle("Cost of a Week's worth of Meals") +# nolint
        theme(
            plot.title = element_text(color = secondary_color, size = title_size),
            axis.title.x = element_text(color = secondary_color, size = axis_font_size),
            axis.title.y = element_text(color = secondary_color, size = axis_font_size) # nolint
        ) +
        xlab("Number of repeated meals") +
        ylab("Price")
}