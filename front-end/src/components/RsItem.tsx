// react
import React from 'react';
import styled from '@emotion/styled';

// store
import { Item } from 'store/model';

export const RsItem = ({ item, style }: RsItemProps) => {
  return (
    <StyledRsItem style={style}>
      <Wrapper>
        <Left>
          <Image>
            <img src={item.icon} alt={item.name} />
          </Image>
          <Text>
            <ItemId>#{item.id}</ItemId>
            <ItemName>{item.name}</ItemName>
          </Text>
        </Left>
      </Wrapper>
    </StyledRsItem>
  );
};

const StyledRsItem = styled.div`
  padding: 48px;
`;

const Wrapper = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;

  padding: 16px 24px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  background: rgba(255, 255, 255, 0.05);
  border-radius: 8px;

  cursor: pointer;
  transition-duration: 0.2s;
  &:hover {
    transform: scale(1.05);
  }
`;

const Left = styled.div`
  display: flex;
  gap: 24px;
`;

const Image = styled.div`
  display: flex;
  align-items: center;
  justify-content: center;
  width: 48px;
  height: 48px;
  background: rgba(255, 255, 255, 0.3);
  border-radius: 99999px;
`;

const Text = styled.div`
  display: flex;
  flex-direction: column;
  gap: 4px;
`;

const ItemId = styled.div`
  font-size: 1rem;
  color: rgba(255, 255, 255, 0.5);
`;

const ItemName = styled.div`
  font-size: 1.5rem;
`;

interface RsItemProps {
  style: any;
  item: Item;
}

RsItem.displayName = 'RsItem';
export default RsItem;
