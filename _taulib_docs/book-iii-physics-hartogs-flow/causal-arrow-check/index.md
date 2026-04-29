---
{
  "projection_kind": "taulib_declaration",
  "title": "causal_arrow_check",
  "permalink": "/verify/taulib/docs/book-iii-physics-hartogs-flow/causal-arrow-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Physics.HartogsFlow`.",
  "declaration_id": "TauLib.BookIII.Physics.HartogsFlow::causal_arrow_check",
  "declaration_slug": "causal-arrow-check",
  "kind": "def",
  "name": "causal_arrow_check",
  "module_name": "TauLib.BookIII.Physics.HartogsFlow",
  "module_url": "/verify/taulib/docs/book-iii-physics-hartogs-flow/",
  "source_line_start": 134,
  "source_line_end": 147,
  "registry_ids": [
    "III.T24"
  ],
  "related_registry_items": [
    {
      "id": "III.T24",
      "title": "Hartogs Flow Theorem",
      "url": "/registry/object/III.T24/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/HartogsFlow.lean#L134-L147",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Physics.HartogsFlow",
        "url": "/verify/taulib/docs/book-iii-physics-hartogs-flow/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/HartogsFlow.lean#L134-L147",
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

- Module: [TauLib.BookIII.Physics.HartogsFlow](/verify/taulib/docs/book-iii-physics-hartogs-flow/)
- Source path: [`TauLib/BookIII/Physics/HartogsFlow.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/HartogsFlow.lean#L134-L147)
- Source range: L134-L147
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T24` — Hartogs Flow Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T24] Causal arrow: the flow is irreversible at the B/C boundary.
    B-part and C-part grow at different rates, creating a natural time arrow. -/
```

## Source Excerpt

```lean
def causal_arrow_check (db : TauIdx) : Bool :=
  go 2 (db + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else
      let b_prod := split_zeta_b k
      let c_prod := split_zeta_c k
      -- B and C products are distinct (asymmetric growth)
      let (b_ct, c_ct, _) := label_counts k
      let asymmetric := if b_ct > 0 && c_ct > 0 then b_prod != c_prod else true
      asymmetric && go (k + 1) (fuel - 1)
  termination_by fuel
```
