---
{
  "projection_kind": "taulib_declaration",
  "title": "topo_translation_check",
  "permalink": "/verify/taulib/docs/book-iii-bridge-translation-topo/topo-translation-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Bridge.TranslationTopo`.",
  "declaration_id": "TauLib.BookIII.Bridge.TranslationTopo::topo_translation_check",
  "declaration_slug": "topo-translation-check",
  "kind": "def",
  "name": "topo_translation_check",
  "module_name": "TauLib.BookIII.Bridge.TranslationTopo",
  "module_url": "/verify/taulib/docs/book-iii-bridge-translation-topo/",
  "source_line_start": 59,
  "source_line_end": 77,
  "registry_ids": [
    "III.D89"
  ],
  "related_registry_items": [
    {
      "id": "III.D89",
      "title": "Topological Translation Functor",
      "url": "/registry/object/III.D89/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationTopo.lean#L59-L77",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Bridge.TranslationTopo",
        "url": "/verify/taulib/docs/book-iii-bridge-translation-topo/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationTopo.lean#L59-L77",
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

- Module: [TauLib.BookIII.Bridge.TranslationTopo](/verify/taulib/docs/book-iii-bridge-translation-topo/)
- Source path: [`TauLib/BookIII/Bridge/TranslationTopo.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationTopo.lean#L59-L77)
- Source range: L59-L77
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D89` — Topological Translation Functor

## Immediate Comment / Docstring

```lean
/-- [III.D89] Tower coherence for translation: π_k ∘ π_{k+1} factors
    through π_k. That is, reduce(reduce(x, k+1), k) = reduce(x, k). -/
```

## Source Excerpt

```lean
def topo_translation_check (bound db : Nat) : Bool :=
  go 0 1 ((bound + 1) * (db + 1))
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k > db then go (x + 1) 1 (fuel - 1)
    else
      let pk := primorial k
      let pk1 := primorial (k + 1)
      if pk == 0 || pk1 == 0 then go x (k + 1) (fuel - 1)
      else
        let xr := x % pk1
        -- Tower coherence: reduce(reduce(x, k+1), k) = reduce(x, k)
        let step1 := reduce xr (k + 1)
        let step2 := reduce step1 k
        let direct := reduce xr k
        (step2 == direct) && go x (k + 1) (fuel - 1)
  termination_by fuel
```
