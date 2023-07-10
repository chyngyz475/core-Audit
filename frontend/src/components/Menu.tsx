import React, { useState } from 'react';
import { AppstoreOutlined, MailOutlined, SettingOutlined, UserOutlined } from '@ant-design/icons';
import type { MenuProps } from 'antd';
import { Menu as AntdMenu, Button } from 'antd';
import { Link } from 'react-router-dom'; // Импортируйте компонент Link из React Router
import Sider from 'antd/es/layout/Sider';
import {
  MenuFoldOutlined,
  MenuUnfoldOutlined,
  UploadOutlined,
  VideoCameraOutlined,
} from '@ant-design/icons';

type MenuItem = Required<MenuProps>['items'][number];

function getItem(
  label: React.ReactNode,
  key: React.Key,
  icon?: React.ReactNode,
  children?: MenuItem[],
  type?: 'item',
  path?: string,
): MenuItem {
  return {
    key,
    icon,
    children,
    label,
    type,
    path,
  } as MenuItem;
}






const Menu: React.FC = () => {
  const onClick: MenuProps['onClick'] = (e) => {
    console.log('click ', e);
  };

  const [collapsed, setCollapsed] = useState(false);
  const onLogoutClick = () => {
    // Handle logout logic
    console.log('Logout clicked');
  };

  return (

      <Sider trigger={null} collapsible collapsed={collapsed}>
        <div className="demo-logo-vertical" />
        <AntdMenu
          mode="inline"
          defaultSelectedKeys={['1']}

        >
          <AntdMenu.Item key="1">

            <span>Deshboard</span>
            <Link to="/Handbook_report" />
          </AntdMenu.Item>
          <AntdMenu.Item key="2">

            <span>Deshboard2</span>
            <Link to="/Handbook_report1" />
          </AntdMenu.Item>
        </AntdMenu>
        <Button icon={<UserOutlined />}>
          <Link to="/login">Авторизация</Link>
        </Button>
        <Button icon={<UserOutlined />}>
          <Link to="/login">Выход</Link>
        </Button>
      </Sider>
      
    
  );
  
};


export default Menu;
