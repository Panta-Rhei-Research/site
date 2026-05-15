---
{
  "projection_kind": "taulib_declaration",
  "title": "representative_entries",
  "permalink": "/corpus/taulib/docs/book-iv-coda-complete-ledger/representative-entries/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Coda.CompleteLedger`.",
  "declaration_id": "TauLib.BookIV.Coda.CompleteLedger::representative_entries",
  "declaration_slug": "representative-entries",
  "kind": "def",
  "name": "representative_entries",
  "module_name": "TauLib.BookIV.Coda.CompleteLedger",
  "module_url": "/corpus/taulib/docs/book-iv-coda-complete-ledger/",
  "source_line_start": 308,
  "source_line_end": 319,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/CompleteLedger.lean#L308-L319",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Coda.CompleteLedger",
        "url": "/corpus/taulib/docs/book-iv-coda-complete-ledger/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/CompleteLedger.lean#L308-L319",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "data/computed value",
      "status": "data/computed value"
    }
  },
  "layout": "taulib-doc",
  "lane": "verify",
  "v2_lane": "verify",
  "status": "Canonical",
  "generated_from": "corpus/taulib-projections",
  "projection_version": "v0.1",
  "canonical_source": "Panta-Rhei-Research/taulib",
  "do_not_edit": true,
  "type": "TauLib Declaration"
}
---

## Declaration Projection

This page is generated directly from the pinned TauLib Lean source snapshot. The source excerpt is public because the active TauLib repository is public.

## Source Provenance

- Module: [TauLib.BookIV.Coda.CompleteLedger](/corpus/taulib/docs/book-iv-coda-complete-ledger/)
- Source path: [`TauLib/BookIV/Coda/CompleteLedger.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/CompleteLedger.lean#L308-L319)
- Source range: L308-L319
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Representative ledger entries (10 of 66, illustrating scope distribution). -/
```

## Source Excerpt

```lean
def representative_entries : List LedgerEntry := [
  ⟨"5 generators", .Established, "structural"⟩,
  ⟨"iota_tau = 2/(pi+e)", .Established, "constant"⟩,
  ⟨"5 self-couplings", .Established, "coupling"⟩,
  ⟨"Temporal complement", .Established, "identity"⟩,
  ⟨"alpha (spectral)", .TauEffective, "coupling"⟩,
  ⟨"R = m_n/m_e (Level 1+)", .TauEffective, "mass ratio"⟩,
  ⟨"M_W = 80.379 GeV", .TauEffective, "mass"⟩,
  ⟨"m_e = 0.510999 MeV", .Conjectural, "mass"⟩,
  ⟨"c_1 = 3/pi", .Conjectural, "correction"⟩,
  ⟨"Penrose tilings", .Metaphorical, "analogy"⟩
]
```
