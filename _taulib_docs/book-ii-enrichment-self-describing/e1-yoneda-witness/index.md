---
{
  "projection_kind": "taulib_declaration",
  "title": "e1_yoneda_witness",
  "permalink": "/verify/taulib/docs/book-ii-enrichment-self-describing/e1-yoneda-witness/",
  "summary_short": "`def` declaration in `TauLib.BookII.Enrichment.SelfDescribing`.",
  "declaration_id": "TauLib.BookII.Enrichment.SelfDescribing::e1_yoneda_witness",
  "declaration_slug": "e1-yoneda-witness",
  "kind": "def",
  "name": "e1_yoneda_witness",
  "module_name": "TauLib.BookII.Enrichment.SelfDescribing",
  "module_url": "/verify/taulib/docs/book-ii-enrichment-self-describing/",
  "source_line_start": 108,
  "source_line_end": 121,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/SelfDescribing.lean#L108-L121",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Enrichment.SelfDescribing",
        "url": "/verify/taulib/docs/book-ii-enrichment-self-describing/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/SelfDescribing.lean#L108-L121",
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

- Module: [TauLib.BookII.Enrichment.SelfDescribing](/verify/taulib/docs/book-ii-enrichment-self-describing/)
- Source path: [`TauLib/BookII/Enrichment/SelfDescribing.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/SelfDescribing.lean#L108-L121)
- Source range: L108-L121
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [II.D57, clause 2] Yoneda witness:
    the pre-Yoneda embedding is faithful -- for the identity function,
    preyoneda_embed_nat(id, x, k) = reduce(x, k), and Code extracts
    the original function value back.

    Concretely: code_extract(f, k, x) = f(reduce(x, k)), so if
    f = id then code_extract(id, k, x) = reduce(x, k) = preyoneda(id, x, k).
    This is the Yoneda lemma in action: the embedding records enough data
    to recover the original map. -/
```

## Source Excerpt

```lean
def e1_yoneda_witness (bound db : TauIdx) : Bool :=
  go 2 1 (bound * db + bound + db + 1)
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k > db then go (x + 1) 1 (fuel - 1)
    else
      let embed_val := preyoneda_embed_nat (fun n => n) x k
      let id_int : TauIdx -> Int := fun n => (n : Int)
      let code_val := code_extract id_int k x
      let ok := embed_val == reduce x k && code_val == (reduce x k : Int)
      ok && go x (k + 1) (fuel - 1)
  termination_by fuel
```
