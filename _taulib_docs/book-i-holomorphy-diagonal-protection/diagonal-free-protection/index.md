---
{
  "projection_kind": "taulib_declaration",
  "title": "diagonal_free_protection",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-diagonal-protection/diagonal-free-protection/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Holomorphy.DiagonalProtection`.",
  "declaration_id": "TauLib.BookI.Holomorphy.DiagonalProtection::diagonal_free_protection",
  "declaration_slug": "diagonal-free-protection",
  "kind": "theorem",
  "name": "diagonal_free_protection",
  "module_name": "TauLib.BookI.Holomorphy.DiagonalProtection",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-diagonal-protection/",
  "source_line_start": 78,
  "source_line_end": 80,
  "registry_ids": [
    "I.T19"
  ],
  "related_registry_items": [
    {
      "id": "I.T19",
      "title": "Diagonal-Free Protection",
      "url": "/registry/object/I.T19/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/DiagonalProtection.lean#L78-L80",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Holomorphy.DiagonalProtection",
        "url": "/verify/taulib/docs/book-i-holomorphy-diagonal-protection/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/DiagonalProtection.lean#L78-L80",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookI.Holomorphy.DiagonalProtection](/verify/taulib/docs/book-i-holomorphy-diagonal-protection/)
- Source path: [`TauLib/BookI/Holomorphy/DiagonalProtection.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/DiagonalProtection.lean#L78-L80)
- Source range: L78-L80
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.T19` — Diagonal-Free Protection

## Immediate Comment / Docstring

```lean
/-- [I.T19] Diagonal-Free Protection Theorem:
    The product of pure B-sector and pure C-sector outputs is always zero.
    This is the structural reflection of e₊·e₋ = 0 at the function level:
    sector-pure outputs cannot combine nontrivially.

    For any two stagewise evaluations giving pure B and pure C outputs,
    their sector product is zero. -/
```

## Source Excerpt

```lean
theorem diagonal_free_protection (b_val c_val : TauIdx) :
    SectorPair.mul ⟨b_val, 0⟩ ⟨0, c_val⟩ = ⟨0, 0⟩ := by
  simp [SectorPair.mul]
```
