---
{
  "projection_kind": "taulib_declaration",
  "title": "tower_decidable_check",
  "permalink": "/verify/taulib/docs/book-iii-bridge-conjecture-gaps/tower-decidable-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Bridge.ConjectureGaps`.",
  "declaration_id": "TauLib.BookIII.Bridge.ConjectureGaps::tower_decidable_check",
  "declaration_slug": "tower-decidable-check",
  "kind": "def",
  "name": "tower_decidable_check",
  "module_name": "TauLib.BookIII.Bridge.ConjectureGaps",
  "module_url": "/verify/taulib/docs/book-iii-bridge-conjecture-gaps/",
  "source_line_start": 173,
  "source_line_end": 182,
  "registry_ids": [
    "III.D111"
  ],
  "related_registry_items": [
    {
      "id": "III.D111",
      "title": "Tower Decidable Check",
      "url": "/registry/object/III.D111/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ConjectureGaps.lean#L173-L182",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Bridge.ConjectureGaps",
        "url": "/verify/taulib/docs/book-iii-bridge-conjecture-gaps/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ConjectureGaps.lean#L173-L182",
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

- Module: [TauLib.BookIII.Bridge.ConjectureGaps](/verify/taulib/docs/book-iii-bridge-conjecture-gaps/)
- Source path: [`TauLib/BookIII/Bridge/ConjectureGaps.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ConjectureGaps.lean#L173-L182)
- Source range: L173-L182
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D111` — Tower Decidable Check

## Immediate Comment / Docstring

```lean
/-- [III.D111] At each finite level, all three conjectures are decidable.
    This is a structural fact: each check function (goldbach_pair,
    twin_prime_count, abc_triple_check) is a computable Lean function.
    Here we verify the structural prerequisites: each conjecture has
    a defined gap type, forbidden move, and scope label. -/
```

## Source Excerpt

```lean
def tower_decidable_check : Bool :=
  -- Each conjecture has a gap type
  let gaps_ok := all_conjectures.all (fun c =>
    (conjecture_gap_type c).toNat <= 2)
  -- Each conjecture maps to a forbidden move
  let fm_ok := all_conjectures.all (fun c =>
    (gap_forbidden_move c).toNat <= 4)
  -- Each conjecture has finite scope (τ-effective) and infinite scope (conjectural)
  let scope_ok := scope_discipline_check
  gaps_ok && fm_ok && scope_ok
```
