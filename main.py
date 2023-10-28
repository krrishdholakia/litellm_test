from fastapi import FastAPI
import os
import litellm, dotenv
import random
dotenv.load_dotenv()
app = FastAPI()

default_messages = [
    """I can't believe how hot it is outside today.""",
    """Have you seen the latest episode of that TV show? It's mind-blowing!""",
    """I had the most delicious dinner at this new restaurant last night.""",
    """Do you have any plans for the weekend?""",
    """I'm feeling really stressed about this upcoming project deadline""",
    """Did you hear about the new store opening in the mall? I'm so excited!""",
    """I just got a puppy, and he's the cutest thing ever!""",
    """I'm struggling with the decision of whether to quit my job or not.""",
    """I passed my driving test today! I'm officially a licensed driver!""",
    """I'm planning a trip to Europe next summer. Any recommendations?""",
    """You know, I've been thinking a lot about the environment lately. It's concerning to see the impact of pollution and climate change on our planet. I believe we all need to take responsibility and make more sustainable choices. By reducing our use of single-use plastics, conserving energy, and supporting renewable energy sources, we can make a positive difference. It's important for individuals, governments, and corporations to come together and implement policies and practices that protect our environment for future generations.""",
    """I recently read this incredible book that completely changed my perspective on life. The author explored themes of self-discovery, resilience, and the power of human connection. It made me reflect on my own journey and the importance of embracing vulnerability. This novel touched my soul and reminded me of the complexity and beauty of human experiences. I think everyone should read it; it truly is a transformative piece of literature.""",
    """Creating a dashboard to view and manage data using Ant Design is simple and straightforward. In this example, we will create a dashboard containing a table and some buttons for managing the data. This assumes you have a working React App and already installed `antd` library. If not, please refer the above instructions to create one.

Step 1: Creating a Dashboard Component

Under the `src` directory, create a new file & name it `Dashboard.js`.

Place the below code inside your `Dashboard.js` file.

```jsx
import React, { useState } from 'react';
import { Table, Button, Space } from 'antd';
import { EditOutlined, DeleteOutlined } from '@ant-design/icons';

const initialData = [
  {
    key: '1',
    name: 'John',
    age: 32,
    address: 'New York',
  },
  {
    key: '2',
    name: 'Jim',
    age: 42,
    address: 'Chicago',
  },
];

const Dashboard = () => {
  const [data, setData] = useState(initialData);

  const handleEdit = (key) => {
    console.log("Edit Record", key);
  }

  const handleDelete = (key) => {
    const filteredData = data.filter(item => item.key!==key);
    setData(filteredData);
  }

  const columns = [
    {
      title: 'Name',
      dataIndex: 'name',
      key: 'name',
    },
    {
      title: 'Age',
      dataIndex: 'age',
      key: 'age',
    },
    {
      title: 'Address',
      dataIndex: 'address',
      key: 'address',
    },
    {
      title: 'Action',
      key: 'action',
      render: (text, record) => (
        <Space size="middle">
          <Button onClick={() => handleEdit(record.key)} icon={<EditOutlined />}>Edit</Button>
          <Button onClick={() => handleDelete(record.key)} icon={<DeleteOutlined />}>Delete</Button>
        </Space>
      ),
    },
  ];

  return (
    <div>
      <h1>Dashboard</h1>
      <Table dataSource={data} columns={columns} />
    </div>
  )
};

export default Dashboard;
```

Step 2: Using Dashboard Component in Your App 

Now navigate to `App.js` and import your `Dashboard` component same as previous example.

```jsx
import React from 'react';
import './App.css';
import 'antd/dist/antd.css';  
import Dashboard from './Dashboard';

function App() {
  return (
    <div className="App">
      <Dashboard />
    </div>
  );
}

export default App;
```

Run your application by using `npm start` in your terminal from your project location. You will see a table with two rows of data with 'Edit' and 'Delete' button columns. When you click 'Delete', the corresponding row will disappear. Clicking 'Edit' logs the key of the row to the console which you can use to update the corresponding data.

This is a simplistic and minimal example of a working dashboard, but you can extend this in many ways, such as adding forms for updating existing data, adding new data, filtering and sorting data, and so on.\n\n--What is the web framework this tutorial is for?.""",
    """Creating a React app that uses Antd (Ant Design) for creating tables, etc. involves several steps. You will first need to set up your React application, then add Antd, and finally add your table. Here's an in-depth guide.

Step 1: Setting up the React application

The easiest way to start a new React app is create-react-app. Open your terminal and type the following command:

```
npx create-react-app react-antd
```
This command will create a new React application with name react-antd. Once it is done, you can switch to the new directory react-antd:

```
cd react-antd
```
Step 2: Installing Antd

You can now install Ant Design in your application. In your terminal type the following command:

```
npm install antd
```

Step 3: Creating an Antd table

Next, you can create a new component that uses an Antd table. Create a new file called MyTable.js in the src folder and paste the following code:

```jsx
import React from 'react';
import { Table } from 'antd';

const dataSource = [
  {
    key: '1',
    name: 'John',
    age: 32,
    address: 'New York',
  },
  {
    key: '2',
    name: 'Jim',
    age: 42,
    address: 'Chicago',
  },
];

const columns = [
  {
    title: 'Name',
    dataIndex: 'name',
    key: 'name',
  },
  {
    title: 'Age',
    dataIndex: 'age',
    key: 'age',
  },
  {
    title: 'Address',
    dataIndex: 'address',
    key: 'address',
  },
];

const MyTable = () => (
  <Table dataSource={dataSource} columns={columns} />
);

export default MyTable;
```

Step 4: Using the Antd table in your app

You can now use MyTable in your main App component. Change the contents of src/App.js to the following:

```jsx
import React from 'react';
import './App.css';
import 'antd/dist/antd.css';  // or 'antd/dist/antd.less'
import MyTable from './MyTable';

function App() {
  return (
    <div className="App">
      <MyTable />
    </div>
  );
}

export default App;
```

Note: You will need to import the Antd css in your main App component (App.js) to ensure the styles are applied. 

That's it. You prepared a React app using Ant Design (antd) for tables. Run your application by using `npm start` in your terminal from your project location. Check your browser, you should see a table with two rows of data. You can update the dataSource and columns array to pass your own data and columns. 

This is a very basic implementation of Antd in React. One of the key aspects of Antd is its component-based philosophy, allowing you to build complex interfaces from small, reusable pieces..\n\n----\n\nWhat is this about?"""
]

@app.get("/chat/completions")
def chat_completions():
    global default_messages
    print("request received")
    message = random.choice(default_messages)
    messages = [{"role": "user", "content": message}]
    response = litellm.completion(model="gpt-3.5-turbo", messages=messages, 
                       fallbacks=[{"model": "azure/gpt-turbo", "api_key": os.getenv("AZURE_FRANCE_API_KEY"), "api_base": os.getenv("AZURE_FRANCE_API_BASE")}, 
                                  {"model": "azure/chatgpt-v-2", "api_key": os.getenv("AZURE_US_EAST_API_KEY"), "api_base": os.getenv("AZURE_US_EAST_API_BASE")},
                                  {"model": "azure/chatgpt-functioncalling", "api_key": os.getenv("AZURE_US_EAST_API_KEY"), "api_base": os.getenv("AZURE_US_EAST_API_BASE")}])
    return response 

@app.get("/")
def hello():
    return {"message": "Hello, World!"}
