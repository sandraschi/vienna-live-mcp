import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { AppLayout } from '@/components/layout/app-layout';
import { Dashboard } from '@/pages/dashboard';
import { Status } from '@/pages/status';
import { Tools } from '@/pages/tools';
import { Chat } from '@/pages/chat';
import { Settings } from '@/pages/settings';
import { Travel } from '@/pages/travel';
import { Shopping } from '@/pages/shopping';
import { Media } from '@/pages/media';
import { Expenses } from '@/pages/expenses';
import { Planning } from '@/pages/planning';
import { Apps } from '@/pages/apps';

function App() {
  return (
    <Router>
      <AppLayout>
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/status" element={<Status />} />
          <Route path="/tools" element={<Tools />} />
          <Route path="/chat" element={<Chat />} />
          <Route path="/settings" element={<Settings />} />
          <Route path="/travel" element={<Travel />} />
          <Route path="/shopping" element={<Shopping />} />
          <Route path="/media" element={<Media />} />
          <Route path="/expenses" element={<Expenses />} />
          <Route path="/planning" element={<Planning />} />
          <Route path="/apps" element={<Apps />} />
          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      </AppLayout>
    </Router>
  );
}

export default App;
