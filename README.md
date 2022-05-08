# GroceryStoreAnalysis
Repository for housing documents, and code for Intro to Statistics 605.631 data challenge.
[Hosted here](https://cjhillbrand-jhu.shinyapps.io/GroceryStoreAnalysis/)
## Ideas for data
1. [Kroger API](https://developer.kroger.com/reference/)
2. Scrape html for safeway
3. Scrape html for trader joes.
4. For recipes

## Ideas for Research Questions
1. How does a no-meat diet compare to a meat-inclusive diet as well a meat-substitute diet.
This question is imprtant since there have been studies, (find study) that show that eating meat has an adverse affect on the environment. Populations are beginning to turn to vegetarianism to aid in reducing their carbon footprint. Likewise companies are trying to find meat-like substitutes that are similar to meat, but not cultivated from livestock. Should a consumer forego buying meat, or should a consumer try meat-substitutes, or should a conusmer adhere to a meat-inclusive diet when considering cost?
2. Is there a price difference between the meals at Kroger, Safeway, and Trader Joes for a weeks worth of meals? A tough choice for any consumer is choosing which grocery store to choose. Doing a plain and simple direct comparison of cost across multiple grocery stores can inform a consumer which store is the correct one for them.
3. Is there a price difference between meal prepping (cooking same thing for 1, 2, ... n meals) versus cooking different things for (1, 2, ... n meals) Consumers can be busy, and a way to save time is to cook once, and meal prep for the upcoming week. Is this tactic actually cheaper? If so how much cheaper? Is there a diminishing affect, such that the more meals you prep the less you may end up saving on the nth meal?
4. Is there a significant price difference between buying the same ingredients in larger quantities and shopping less versus buying less quantities more frequenty. This is the classic question of buying in bulk versus buying a little each visit. For this analysis to be honest, expiration dates and outlining the frequency in which the product is consumed can help put this question into a different light. If you buy in bulk you may save more, but how much of that is being thrown out?
5. Are stores that sell food items at lower prices less accessible than stores that offer food items at higher prices. 

## Data Model
Grocery Store Products
| Name | Description |
|------|-------------|
| Grocery Store | Name of the store the product is from |
| Quantity | The sale quantity of the item |
| Price | The price of the specified quantity |
| Name | Title of the product |
| GPID | Unique Id of product |

Products Mapping 
| Name | Descritpion |
|-|-|
| GPID | FK to the Grocery Store Product table |
| PID | FK to the Recipe Table

Recipes Table
| Name | Description |
|-|-|
| Recipe Name | Name of the recipe |
| RID | Unique identifier of the recipe |
| Health Score | System given score of how healthy. |
| Servings  | Number of servings the recipe serves |
| Vegetarian | If the recipe is vegetarian |
| type | Whether the meal is for breakfast lunch or dinner. |

Ingredients Table 
| Name | Description |
| - | - |
| RID | FK to recipe |
| PID | PK to products mapping |
| Name | the name of the ingredient |
| Amount | the normalized amount of the ingredient |
| Unit | How the amount is measured |

Nutrition Table
| Name | Description | 
| - | - |
| RID | FK to recipe |
| protein | protein contained in recipe for 1 serving |
| Fat | fat contained in recipe for 1 serving |
| Carbs | carbs contained in recipe for 1 serving |
| calories | calories for 1 serving |