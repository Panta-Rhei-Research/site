---
{
  "projection_kind": "taulib_declaration",
  "title": "remark_oq_a3_resolved",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-weinberg-nlo/remark-oq-a3-resolved/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Electroweak.WeinbergNLO`.",
  "declaration_id": "TauLib.BookIV.Electroweak.WeinbergNLO::remark_oq_a3_resolved",
  "declaration_slug": "remark-oq-a3-resolved",
  "kind": "def",
  "name": "remark_oq_a3_resolved",
  "module_name": "TauLib.BookIV.Electroweak.WeinbergNLO",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-weinberg-nlo/",
  "source_line_start": 196,
  "source_line_end": 197,
  "registry_ids": [
    "IV.R390"
  ],
  "related_registry_items": [
    {
      "id": "IV.R390",
      "title": "OQ-A3 Resolution Status",
      "url": "/registry/object/IV.R390/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L196-L197",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.WeinbergNLO",
        "url": "/verify/taulib/docs/book-iv-electroweak-weinberg-nlo/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/verify/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L196-L197",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
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

- Module: [TauLib.BookIV.Electroweak.WeinbergNLO](/verify/taulib/docs/book-iv-electroweak-weinberg-nlo/)
- Source path: [`TauLib/BookIV/Electroweak/WeinbergNLO.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L196-L197)
- Source range: L196-L197
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.R390` — OQ-A3 Resolution Status

## Immediate Comment / Docstring

```lean
/-- [IV.R390] OQ-A3 (M_W/m_n direct formula) is RESOLVED:
    1. w = (17/5)·ι⁻³ has CF window algebra motivation (W₃(3)/W₃(4)).
    2. The 250 ppm gap is a tree-level Sirlin remainder.
    3. w does NOT appear in the Fermi form — the gap is physically inert.
    4. The tree-level Sirlin relation necessarily produces ~2-3% gap
       (radiative corrections to M_W are well-understood in the SM).
    5. Mode interpretation: 17 = n_total + n_A, 5 = n_B + n_A. -/
```

## Source Excerpt

```lean
def remark_oq_a3_resolved : String :=
  "OQ-A3 RESOLVED: w cancels in Fermi form; 250 ppm is tree-level Sirlin remainder."
```
