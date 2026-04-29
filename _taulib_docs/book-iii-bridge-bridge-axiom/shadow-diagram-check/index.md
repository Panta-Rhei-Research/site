---
{
  "projection_kind": "taulib_declaration",
  "title": "shadow_diagram_check",
  "permalink": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/shadow-diagram-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Bridge.BridgeAxiom`.",
  "declaration_id": "TauLib.BookIII.Bridge.BridgeAxiom::shadow_diagram_check",
  "declaration_slug": "shadow-diagram-check",
  "kind": "def",
  "name": "shadow_diagram_check",
  "module_name": "TauLib.BookIII.Bridge.BridgeAxiom",
  "module_url": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/",
  "source_line_start": 148,
  "source_line_end": 169,
  "registry_ids": [
    "III.D72"
  ],
  "related_registry_items": [
    {
      "id": "III.D72",
      "title": "Shadow Diagram",
      "url": "/registry/object/III.D72/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/BridgeAxiom.lean#L148-L169",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Bridge.BridgeAxiom",
        "url": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/BridgeAxiom.lean#L148-L169",
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

- Module: [TauLib.BookIII.Bridge.BridgeAxiom](/verify/taulib/docs/book-iii-bridge-bridge-axiom/)
- Source path: [`TauLib/BookIII/Bridge/BridgeAxiom.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/BridgeAxiom.lean#L148-L169)
- Source range: L148-L169
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D72` — Shadow Diagram

## Immediate Comment / Docstring

```lean
/-- [III.D72] Shadow diagram: the image of a tau-internal diagram under
    the bridge functor. A shadow preserves commutativity but may lose
    injectivity or faithfulness at forbidden moves.

    Modeled as: for a commutative square (a -> b -> c) in tau,
    the shadow (F(a) -> F(b) -> F(c)) in ZFC preserves the composition
    (reduce coherence) but may collapse distinct values. -/
```

## Source Excerpt

```lean
def shadow_diagram_check (bound db : TauIdx) : Bool :=
  go 0 0 1 ((bound + 1) * (bound + 1) * (db + 1))
where
  go (a b k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if a > bound then true
    else if b > bound then go (a + 1) 0 1 (fuel - 1)
    else if k > db then go a (b + 1) 1 (fuel - 1)
    else
      let pk := primorial k
      if pk == 0 then go a b (k + 1) (fuel - 1)
      else
        let ar := a % pk
        let br := b % pk
        -- tau-internal composition: reduce(a + b, k)
        let tau_compose := reduce ((ar + br) % pk) k
        -- Shadow composition: reduce(a, k) + reduce(b, k) mod Prim(k)
        let shadow_compose := (reduce ar k + reduce br k) % pk
        -- Commutativity preserved (shadow agrees with tau composition)
        let commutes := tau_compose == shadow_compose
        commutes && go a b (k + 1) (fuel - 1)
  termination_by fuel
```
