STORES <- c("Safeway", "Trader Joe\'s", "Fred Meyer - Ballard")

hist_tab_panel <- function(title, id, sidebar_column=NULL, sidebar_column_width=0) {
    main_plot_width <- 12 - sidebar_column_width
    tabPanel(
        title,
        fluidRow(
            column(main_plot_width, plotOutput(outputId = paste0(id, "_hist"))), 
            sidebar_column),
        verbatimTextOutput(outputId = paste0(id, "_summary")),
        verbatimTextOutput(outputId = paste0(id, "_test"))
    )
}

fluidPage(
    titlePanel("Grocery Store Analysis"),
    tabsetPanel(type = "tabs",
        hist_tab_panel(
            "Store Product Data",
            "store",
            column(
                2,
                radioButtons("store_one", "Store One:", STORES, selected = STORES[1]),
                radioButtons("store_two", "Store Two:", STORES, selected = STORES[2])), 2),
        hist_tab_panel("Organic Product Data", "organic"),
        hist_tab_panel("Bulk Product Data", "bulk"),
        hist_tab_panel("Vegetarian Comparison Data", "vegetarian"),
        tabPanel(
            "Meal Planning Analysis",
            plotOutput("meal_plan_plot"),
            verbatimTextOutput("meal_plan_summary"))
    )
)