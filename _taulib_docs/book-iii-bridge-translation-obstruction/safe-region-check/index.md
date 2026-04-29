---
{
  "projection_kind": "taulib_declaration",
  "title": "safe_region_check",
  "permalink": "/verify/taulib/docs/book-iii-bridge-translation-obstruction/safe-region-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Bridge.TranslationObstruction`.",
  "declaration_id": "TauLib.BookIII.Bridge.TranslationObstruction::safe_region_check",
  "declaration_slug": "safe-region-check",
  "kind": "def",
  "name": "safe_region_check",
  "module_name": "TauLib.BookIII.Bridge.TranslationObstruction",
  "module_url": "/verify/taulib/docs/book-iii-bridge-translation-obstruction/",
  "source_line_start": 165,
  "source_line_end": 184,
  "registry_ids": [
    "III.T61"
  ],
  "related_registry_items": [
    {
      "id": "III.T61",
      "title": "Translation Failure Boundary",
      "url": "/registry/object/III.T61/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationObstruction.lean#L165-L184",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationObstruction.lean#L165-L184",
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
- Source path: [`TauLib/BookIII/Bridge/TranslationObstruction.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationObstruction.lean#L165-L184)
- Source range: L165-L184
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T61` — Translation Failure Boundary

## Immediate Comment / Docstring

```lean
/-- [III.T61] Safe region check: within the safe region (no forbidden
    moves invoked), both translations are perfectly faithful. -/
```

## Source Excerpt

```lean
def safe_region_check (bound db : Nat) : Bool :=
  go 0 1 ((bound + 1) * (db + 1))
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k > db then go (x + 1) 1 (fuel - 1)
    else
      let pk := primorial k
      if pk == 0 then go x (k + 1) (fuel - 1)
      else
        let xr := x % pk
        -- In the safe region: reduce-stable, bounded, and canonical
        let safe := reduce xr k == xr && xr < pk
        -- If safe, arithmetic translation is faithful
        let arith_ok := !safe || arith_translate xr k == xr
        -- If safe, topological projection commutes
        let topo_ok := !safe || tower_projection xr k == xr
        arith_ok && topo_ok && go x (k + 1) (fuel - 1)
  termination_by fuel
```
