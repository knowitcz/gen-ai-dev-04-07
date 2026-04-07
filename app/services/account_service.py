import logging
from app.models.account import Account
from app.repository.account_repository import AccountRepository

logger = logging.getLogger(__name__)


class AccountService(object):
    def __init__(self, account_repository: AccountRepository):
        self.account_repository = account_repository

    def get_account_by_id(self, account_id: int) -> Account | None:
        """
        Get account by ID
        """
        logger.debug(f"Fetching account with ID: {account_id}")
        account = self.account_repository.get_by_id(account_id)
        if account:
            logger.info(f"Account {account_id} retrieved successfully")
        else:
            logger.warning(f"Account {account_id} not found")
        return account

    def transfer_money(self, from_account_id: int, to_account_id: int, amount: int) -> None:
        """
        Transfer money from one account to another within a single transaction
        """
        logger.info(f"Transfer initiated: {amount} from account {from_account_id} to {to_account_id}")
        try:
            with self.account_repository.session.begin():
                self.account_repository.withdraw_money(from_account_id, amount)
                self.account_repository.deposit_money(to_account_id, amount)
            logger.info(f"Transfer completed successfully: {amount} from {from_account_id} to {to_account_id}")
        except Exception as e:
            logger.error(f"Transfer failed: {e}", exc_info=True)
            raise

    def withdraw_money(self, account_id: int, amount: int) -> None:
        """
        Withdraw money from an account
        """
        logger.info(f"Withdrawal initiated: {amount} from account {account_id}")
        try:
            with self.account_repository.session.begin():
                self.account_repository.withdraw_money(account_id, amount)
            logger.info(f"Withdrawal completed: {amount} from account {account_id}")
        except Exception as e:
            logger.error(f"Withdrawal failed: {e}", exc_info=True)
            raise

    def deposit_money(self, account_id: int, amount: int) -> None:
        """
        Deposit money into an account
        """
        logger.info(f"Deposit initiated: {amount} to account {account_id}")
        try:
            with self.account_repository.session.begin():
                self.account_repository.deposit_money(account_id, amount)
            logger.info(f"Deposit completed: {amount} to account {account_id}")
        except Exception as e:
            logger.error(f"Deposit failed: {e}", exc_info=True)
            raise
