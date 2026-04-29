---
{
  "projection_kind": "taulib_declaration",
  "title": "rewiring_levels_eq_solenoidal",
  "permalink": "/verify/taulib/docs/book-i-kernel-diagonal/rewiring-levels-eq-solenoidal/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Kernel.Diagonal`.",
  "declaration_id": "TauLib.BookI.Kernel.Diagonal::rewiring_levels_eq_solenoidal",
  "declaration_slug": "rewiring-levels-eq-solenoidal",
  "kind": "theorem",
  "name": "rewiring_levels_eq_solenoidal",
  "module_name": "TauLib.BookI.Kernel.Diagonal",
  "module_url": "/verify/taulib/docs/book-i-kernel-diagonal/",
  "source_line_start": 77,
  "source_line_end": 79,
  "registry_ids": [
    "I.D03"
  ],
  "related_registry_items": [
    {
      "id": "I.D03",
      "title": "Diagonal Discipline",
      "url": "/registry/object/I.D03/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Diagonal.lean#L77-L79",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Kernel.Diagonal",
        "url": "/verify/taulib/docs/book-i-kernel-diagonal/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Diagonal.lean#L77-L79",
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

- Module: [TauLib.BookI.Kernel.Diagonal](/verify/taulib/docs/book-i-kernel-diagonal/)
- Source path: [`TauLib/BookI/Kernel/Diagonal.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Diagonal.lean#L77-L79)
- Source range: L77-L79
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.D03` — Diagonal Discipline

## Immediate Comment / Docstring

```lean
/-- [I.D03] The diagonal discipline: exactly 3 rewiring levels exist
    because exactly 3 solenoidal generators are available as targets.
    Each rewiring level consumes one generator:
    - Level 1 (addition) ↔ π
    - Level 2 (multiplication) ↔ γ
    - Level 3 (exponentiation) ↔ η
    No 4th level: α is the counting scaffold, ω is the beacon. -/
```

## Source Excerpt

```lean
theorem rewiring_levels_eq_solenoidal :
    solenoidalGenerators.length = nonOmegaGenerators.length - 1 := by
  rfl
```
