---
{
  "projection_kind": "taulib_declaration",
  "title": "obstruction_check",
  "permalink": "/verify/taulib/docs/book-iii-bridge-translation-obstruction/obstruction-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Bridge.TranslationObstruction`.",
  "declaration_id": "TauLib.BookIII.Bridge.TranslationObstruction::obstruction_check",
  "declaration_slug": "obstruction-check",
  "kind": "def",
  "name": "obstruction_check",
  "module_name": "TauLib.BookIII.Bridge.TranslationObstruction",
  "module_url": "/verify/taulib/docs/book-iii-bridge-translation-obstruction/",
  "source_line_start": 102,
  "source_line_end": 121,
  "registry_ids": [
    "III.D91"
  ],
  "related_registry_items": [
    {
      "id": "III.D91",
      "title": "Obstruction Cocycle",
      "url": "/registry/object/III.D91/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationObstruction.lean#L102-L121",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Bridge.TranslationObstruction",
        "url": "/verify/taulib/docs/book-iii-bridge-translation-obstruction/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationObstruction.lean#L102-L121",
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

- Module: [TauLib.BookIII.Bridge.TranslationObstruction](/verify/taulib/docs/book-iii-bridge-translation-obstruction/)
- Source path: [`TauLib/BookIII/Bridge/TranslationObstruction.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationObstruction.lean#L102-L121)
- Source range: L102-L121
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D91` — Obstruction Cocycle

## Immediate Comment / Docstring

```lean
/-- [III.D91] Obstruction check: verify obstruction values match
    expected damage levels. -/
```

## Source Excerpt

```lean
def obstruction_check (db : Nat) : Bool :=
  go 1 (db + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else
      -- Mild obstructions (damage ≤ 1): value is bounded or 0
      let mild_ok :=
        obstruction_value .global_equality k == 0 &&
        obstruction_value .nonlocal_disguise k == 0
      -- Severe obstructions (damage 2): value grows but bounded by k
      let severe_ok :=
        obstruction_value .unbounded_fanout k == k
      -- Breaking obstructions (damage 3): value grows with M_k
      let break_ok :=
        obstruction_value .succinct_circuits k > 0 &&
        obstruction_value .exponential_quantification k > 0
      mild_ok && severe_ok && break_ok && go (k + 1) (fuel - 1)
  termination_by fuel
```
