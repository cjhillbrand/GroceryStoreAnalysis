# server.R
source("dataManager.r")
source("components.r")
function(input, output) {
    bulk_data <- get_bulk_data()
    organic_data <- get_organic_data()
    recipe_data <- get_recipe_data()

    output$bulk_hist <- renderPlot({
        create_price_diff_hist(bulk_data, "Bulk", "Non-Bulk")
    })

    output$bulk_summary <- renderPrint({
        summary(bulk_data$price_diff)
    })

    output$bulk_test <- renderPrint({
        t.test(bulk_data$price_diff, mu = 0)
    })

    output$organic_hist <- renderPlot({
        create_price_diff_hist(organic_data, "Organic", "Non-Organic")
    })

    output$organic_summary <- renderPrint({
        summary(organic_data$price_diff)
    })

    output$organic_test <- renderPrint({
        t.test(organic_data$price_diff, mu = 0)
    })

    store_data <- reactive({
        get_grocery_store_data(input$store_one, input$store_two)
    })

    output$store_hist <- renderPlot({
        create_price_diff_hist(store_data(), input$store_one, input$store_two)
    })

    output$store_summary <- renderPrint({
        summary(store_data()$price_diff)
    })

    output$store_test <- renderPrint({
        t.test(store_data()$price_diff, mu = 0)
    })

    output$vegetarian_hist <- renderPlot({
        create_price_comp_hist(recipe_data)
    })

    output$vegetarian_summary <- renderPrint({
        print("Summary for Vegetarian Recipes")
        print(summary(recipe_data[recipe_data$vegetarian == 1, ]$price))

        print("Summary for Non-Vegetarian Recipes")
        print(summary(recipe_data[recipe_data$vegetarian == 0, ]$price))
    })

    output$vegetarian_test <- renderPrint({
        dist_one <- recipe_data[recipe_data$vegetarian == 1, ]$price
        dist_two <- recipe_data[recipe_data$vegetarian == 0, ]$price
        t.test(dist_one, dist_two, var.equal = TRUE)
    })

    breakfast_prices <- recipe_data[recipe_data$type == "breakfast", ]$price
    main_prices <- recipe_data[recipe_data$type == "main course", ]$price
    get_meal_plan_price <- function(repeats) {
        b_prices <- sample(breakfast_prices, 7)
        m_prices <- sample(main_prices, 14 - repeats)
        result <- sum(b_prices) + sum(m_prices)
        if (repeats > 0) {
            result <- result + sum(rep(m_prices[0], repeats - 1))
        }

        result
    }

    repeats <- seq(0, 13)
    iters <- 10
    x <- rep(repeats, iters)
    y <- sapply(x, get_meal_plan_price)
    meal_plan_data <- data.frame(repeats = x, price = y)
    regression_line <- lm(repeats~price, meal_plan_data)
    output$meal_plan_plot <- renderPlot({
        create_linear_regression_plot(meal_plan_data)
    })

    output$meal_plan_summary <- renderPrint({
        summary(regression_line)
    })
}
