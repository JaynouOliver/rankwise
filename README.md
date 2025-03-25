# rankwise
RankWise is a Python library that leverages large language models to evaluate and sort data based on quality rather than quantity. Applicable across diverse domains, RankWise provides a universal framework for assessing code, text, and multimedia, ensuring fair and insightful evaluations.



## Usage

Export your OpenAI API key:


Format your data as follows:

```
commits = [
    
    CommitData(
        commit_id="a1b2c",
        details="fixed cuda kernels",
        rank=1
    ),
    
]
```


Sort using RankWise:


from rankwise.llm_sort import llm_bubble_sort

sorted_commits = llm_bubble_sort(commits)
print(sorted_commits)


## Contributing

We welcome contributions! Please submit pull requests or report issues on GitHub.


LLMsorting.py works fine as of now. 
please try that. 

We have future plans to add local models from Ollama to run on CPU, write imporved algorithms like python.sort() algos, make it sector agnostic so that you can rank any data.