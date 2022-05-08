library(RSQLite)
library(stringr)
DATA_DIR <- ".data/"
DATA_FILE <- paste0(DATA_DIR, "grocery_store_analysis.db")

QUERIES_DIR <- paste0(DATA_DIR, "queries/")
BULK_QUERY_FILE <- paste0(QUERIES_DIR, "getBulkData.sql")
ORGANIC_QUERY_FILE <- paste0(QUERIES_DIR, "getOrganicData.sql")
PRODUCTS_QUERY_FILE <- paste0(QUERIES_DIR, "getProducts.sql")
RECIPES_QUERY_FILE <- paste0(QUERIES_DIR, "getRecipes.sql")

con <- dbConnect(RSQLite::SQLite(), DATA_FILE)

fetch_results <- function(sql_select) {
    res <- dbSendQuery(con, sql_select)
    dbFetch(res)
}

issue_sql_select <- function(sql_file) {
    sql_select <- read_file(sql_file)
    fetch_results(sql_select)
}

read_file <- function(file_name) {
    paste(readLines(file_name), collapse = " ")
}

get_recipe_data <- function() {
    issue_sql_select(RECIPES_QUERY_FILE)
}

get_grocery_store_data <- function(store_one, store_two) {
    query <- read_file(PRODUCTS_QUERY_FILE)
    store_one <- sub("\'", "\'\'", store_one)
    store_two <- sub("\'", "\'\'", store_two)
    query <- sub("STORE_ONE", store_one, query)
    query <- sub("STORE_TWO", store_two, query)
    fetch_results(query)
}

get_organic_data <- function() {
    issue_sql_select(ORGANIC_QUERY_FILE)
}

get_bulk_data <- function() {
    issue_sql_select(BULK_QUERY_FILE)
}
